/**
 * The JESD204 framework
 *
 * Copyright (c) 2019 Analog Devices Inc.
 *
 * This program is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License version 2 as published by
 * the Free Software Foundation.
 */

#define pr_fmt(fmt) "jesd204: " fmt

#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/device.h>
#include <linux/debugfs.h>
#include <linux/of.h>
#include <linux/slab.h>

#include "jesd204-priv.h"

static dev_t jesd204_devt;

static DEFINE_MUTEX(jesd204_device_list_lock);
static LIST_HEAD(jesd204_device_list);
static LIST_HEAD(jesd204_topologies);

static unsigned int jesd204_device_count;
static unsigned int jesd204_topologies_count;

#define JESD204_DEV_MAX 256
static struct bus_type jesd204_bus_type = {
	.name = "jesd204",
};

static struct dentry *jesd204_debugfs_dentry;

static struct jesd204_dev *jesd204_dev_alloc(struct device_node *np)
{
	struct jesd204_dev_top *jdev_top;
	struct jesd204_dev *jdev;
	bool is_top = of_property_read_bool(np, "jesd204-top-device");

	if (is_top) {
		jdev_top = kzalloc(sizeof(*jdev_top), GFP_KERNEL);
		if (!jdev_top)
			return ERR_PTR(-ENOMEM);

		jdev = &jdev_top->jdev;
		list_add(&jdev_top->list, &jesd204_topologies);
		jesd204_topologies_count++;
	} else {
		jdev = kzalloc(sizeof(*jdev), GFP_KERNEL);
		if (!jdev)
			return ERR_PTR(-ENOMEM);
	}

        kref_get(&jdev->ref);

	jdev->is_top = is_top;
	jdev->np = of_node_get(np);
	kref_init(&jdev->ref);

	list_add(&jdev->list, &jesd204_device_list);
	jesd204_device_count++;

	return jdev;
}

static struct jesd204_dev *jesd204_dev_find_by_of_node(struct device_node *np)
{
	struct jesd204_dev *jdev = NULL, *jdev_it;

	if (!np)
		return NULL;

	list_for_each_entry(jdev_it, &jesd204_device_list, list) {
		if (jdev_it->np == np) {
			jdev = jdev_it;
			break;
		}
	}

	return jdev;
}

static int jesd204_of_create_devices(void)
{
	struct jesd204_dev *jdev;
	struct device_node *np;
	int ret;

	mutex_lock(&jesd204_device_list_lock);

	ret = 0;
	for_each_node_with_property(np, "jesd204-device") {
		jdev = jesd204_dev_alloc(np);
		if (IS_ERR(jdev)) {
			ret = PTR_ERR(jdev);
			goto unlock;
		}
	}

unlock:
	mutex_unlock(&jesd204_device_list_lock);

	return ret;
}

struct jesd204_dev *jesd204_dev_register(struct device *dev,
					 const struct jesd204_dev_data *init)
{
	struct jesd204_dev *jdev;
	int ret;

	if (!dev)
		return ERR_PTR(-EINVAL);

	if (!init)
		return ERR_PTR(-EINVAL);

	mutex_lock(&jesd204_device_list_lock);

	jdev = jesd204_dev_find_by_of_node(dev->of_node);
	if (!jdev) {
		ret = -ENODEV;
		goto err;
	}

	jdev->ops = init->ops;
	jdev->dev = get_device(dev);

	mutex_unlock(&jesd204_device_list_lock);

	return jdev;
err:
	mutex_unlock(&jesd204_device_list_lock);

	return ERR_PTR(ret);
}
EXPORT_SYMBOL(jesd204_dev_register);

static void jesd204_of_unregister_devices(void)
{
	struct jesd204_dev *jdev, *j;

	list_for_each_entry_safe(jdev, j, &jesd204_device_list, list) {
		jesd204_dev_unregister(jdev);
	}
}

/* Free memory allocated. */
static void __jesd204_dev_release(struct kref *ref)
{
	struct jesd204_dev *jdev = container_of(ref, struct jesd204_dev, ref);
	struct jesd204_dev_top *jdev_top;

	mutex_lock(&jesd204_device_list_lock);

	if (jdev->dev)
		put_device(jdev->dev);

	if (jdev->is_top) {
		jdev_top = jesd204_dev_top_dev(jdev);
		if (jdev_top) {
			list_del(&jdev_top->list);
			jesd204_topologies_count--;
		}
	} else
		jdev_top = NULL;

	list_del(&jdev->list);
	of_node_put(jdev->np);

	if (jdev_top)
		kfree(jdev_top);
	else
		kfree(jdev);

	jesd204_device_count--;

	mutex_unlock(&jesd204_device_list_lock);
}

/**
 * jesd204_dev_unregister() - unregister a device from the JESD204 subsystem
 * @jdev:		Device structure representing the device.
 **/
void jesd204_dev_unregister(struct jesd204_dev *jdev)
{
	if (!IS_ERR_OR_NULL(jdev))
		return;

	kref_put(&jdev->ref, __jesd204_dev_release);
}
EXPORT_SYMBOL(jesd204_dev_unregister);

static int __init jesd204_init(void)
{
	int ret;

	/* Register sysfs bus */
	ret = bus_register(&jesd204_bus_type);
	if (ret < 0) {
		pr_err("could not register bus type\n");
		goto error_nothing;
	}

	ret = alloc_chrdev_region(&jesd204_devt, 0, JESD204_DEV_MAX, "jesd204");
	if (ret < 0) {
		pr_err("failed to allocate char dev region\n");
		goto error_unregister_bus_type;
	}

	jesd204_debugfs_dentry = debugfs_create_dir("jesd204", NULL);

	mutex_init(&jesd204_device_list_lock);

	ret = jesd204_of_create_devices();
	if (ret < 0)
		goto error_unreg_devices;

	return 0;

error_unreg_devices:
	jesd204_of_unregister_devices();
error_unregister_bus_type:
	bus_unregister(&jesd204_bus_type);
error_nothing:
	pr_err("framework error: %d\n", ret);
	return ret;
}

static void __exit jesd204_exit(void)
{
	jesd204_of_unregister_devices();
	if (jesd204_devt)
		unregister_chrdev_region(jesd204_devt, JESD204_DEV_MAX);
	bus_unregister(&jesd204_bus_type);
	debugfs_remove_recursive(jesd204_debugfs_dentry);
	mutex_destroy(&jesd204_device_list_lock);
}

subsys_initcall(jesd204_init);
module_exit(jesd204_exit);

MODULE_AUTHOR("Alexandru Ardelean <alexandru.ardelean@analog.com>");
MODULE_DESCRIPTION("JESD204 core");
MODULE_LICENSE("GPL");
