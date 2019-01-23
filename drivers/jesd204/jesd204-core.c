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

	INIT_LIST_HEAD(&jdev->top_devices);
	INIT_LIST_HEAD(&jdev->outputs);

	list_add(&jdev->list, &jesd204_device_list);
	jesd204_device_count++;

	return jdev;
}

static int jesd204_dev_set_error(struct jesd204_dev *jdev, int err)
{
	struct jesd204_dev_top *jdev_top;
	struct jesd204_dev_list *e;

	if (err == 0)
		return 0;

	/* we aready have an error state */
	if (jdev->error)
		return err;

	jdev->error = err;

	jdev_top = jesd204_dev_top_dev(jdev);
	if (jdev_top)
		jdev_top->error = true;

	/* tell all top devices about the error */
	list_for_each_entry(e, &jdev->top_devices, list) {
		jdev_top = jesd204_dev_top_dev(e->jdev);
		jdev_top->error = true;
	}

	return err;
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

static struct jesd204_dev_link *jesd204_dev_find_output_link(
		struct jesd204_dev *jdev,
		struct of_phandle_args *args)
{
	struct jesd204_dev_link *lnk;
	unsigned int i;

	/* find an existing output link for the current of args */
	list_for_each_entry(lnk, &jdev->outputs, list) {
		if (args->np != lnk->of.np)
			continue;
		if (args->args_count != lnk->of.args_count)
			continue;
		for (i = 0; i < args->args_count; i++) {
			if (args->args[i] != lnk->of.args[i])
				break;
		}
		if (i != args->args_count)
			continue;
		return lnk;
	}

	return NULL;
}

static int jesd204_dev_propagate_cb_inputs(struct jesd204_dev *jdev,
					   jesd204_cb_priv propagated_cb,
					   void *data)
{
	unsigned int i;
	int ret = 0;

	for (i = 0; i < jdev->inputs_count; i++) {
		struct jesd204_dev_link *lnk = jdev->inputs[i];

		ret = jesd204_dev_propagate_cb_inputs(lnk->owner,
						      propagated_cb, data);
		if (ret)
			goto done;
		ret = propagated_cb(lnk->owner, data);
		if (ret)
			goto done;
	}

done:
	return jesd204_dev_set_error(jdev, ret);
}

static int jesd204_dev_propagate_cb_outputs(struct jesd204_dev *jdev,
					    jesd204_cb_priv propagated_cb,
					    void *data)
{
	struct jesd204_dev_link *l;
	struct jesd204_dev_list *e;
	int ret = 0;

	list_for_each_entry(l, &jdev->outputs, list) {
		list_for_each_entry(e, &l->dests, list) {
			ret = propagated_cb(e->jdev, data);
			if (ret)
				goto done;
			ret = jesd204_dev_propagate_cb_outputs(e->jdev,
							       propagated_cb,
							       data);
			if (ret)
				goto done;
		}
	}

done:
	return jesd204_dev_set_error(jdev ,ret);
}

static inline int jesd204_dev_propagate_cb(struct jesd204_dev *jdev,
					   jesd204_cb_priv propagated_cb,
					   void *data)
{
	int ret;

	ret = jesd204_dev_propagate_cb_inputs(jdev, propagated_cb, data);
	if (ret)
		return ret;

	return jesd204_dev_propagate_cb_outputs(jdev, propagated_cb, data);
}

static int jesd204_dev_create_link(struct jesd204_dev *jdev,
				   struct of_phandle_args *args)
{
	struct jesd204_dev_link *lnk;
	struct jesd204_dev *jdev_in;
	struct jesd204_dev_list *e;

	jdev_in = jesd204_dev_find_by_of_node(args->np);
	if (!jdev_in) {
		pr_err("link %pOF->%pOF invalid\n", args->np, jdev->np);
		return -ENOENT;
	}

	e = kzalloc(sizeof(*e), GFP_KERNEL);
	if (!e)
		return -ENOMEM;

	lnk = jesd204_dev_find_output_link(jdev_in, args);
	if (!lnk) {
		lnk = kzalloc(sizeof(*lnk), GFP_KERNEL);
		if (!lnk) {
			kfree(e);
			return -ENOMEM;
		}

		lnk->owner = jdev_in;
		INIT_LIST_HEAD(&lnk->dests);

		memcpy(&lnk->of, args, sizeof(lnk->of));
		list_add(&lnk->list, &jdev_in->outputs);
	}

	e->jdev = jdev;
	list_add(&e->list, &lnk->dests);

	/* increment kref on both sides */
	kref_get(&jdev_in->ref);
	kref_get(&jdev->ref);

	jdev->inputs[jdev->inputs_count] = lnk;
	jdev->inputs_count++;

	return 0;
}

static int jesd204_of_device_create_links(struct jesd204_dev *jdev)
{
	struct device_node *np = jdev->np;
	struct of_phandle_args args;
	int i, c, ret;

	c = of_count_phandle_with_args(np, "jesd204-inputs", "#jesd204-cells");
	if (c == -ENOENT || c == 0)
		return 0;
	if (c < 0)
		return c;

	jdev->inputs = kcalloc(c, sizeof(*jdev->inputs), GFP_KERNEL);
	if (!jdev->inputs)
		return -ENOMEM;

	for (i = 0; i < c; i++) {
		ret = of_parse_phandle_with_args(np,
						 "jesd204-inputs",
						 "#jesd204-cells",
						 i, &args);
		/**
		 * If one bad/non-existing link is found, then all
		 * JESD204 topologies won't be initialized. We may
		 * improve this later, to allow the good configs
		 */
		if (ret < 0)
			return ret;

		ret = jesd204_dev_create_link(jdev, &args);
		if (ret) {
			of_node_put(args.np);
			return ret;
		}
	}

	return 0;
}

static void __jesd204_dev_top_state_change_cb(struct kref *ref)
{
	struct jesd204_dev_top *jdev_top;
	struct jesd204_dev *jdev;
	int ret;

	jdev_top = container_of(ref, typeof(*jdev_top), cb_ref);
	jdev = &jdev_top->jdev;

	jdev->state = jdev_top->nxt_state;
	if (jdev_top->state_complete_cb) {
		ret = jdev_top->state_complete_cb(jdev);
		jesd204_dev_set_error(jdev, ret);
	}

	/**
	 * Reset nxt_state ; so that other devices won't run another
	 * state change
	 */
	jdev_top->nxt_state = 0;
}

static int jesd204_dev_notify_state_change(struct jesd204_dev *jdev)
{
	struct jesd204_dev_top *jdev_top;
	struct jesd204_dev_list *e;

	/**
	 * Now go through the list of top devices (that this device cares about)
	 * and see which device we need to notify/update
	 */
	list_for_each_entry(e, &jdev->top_devices, list) {
		jdev_top = jesd204_dev_top_dev(e->jdev);

		/**
		 * Propagate to top devices that want to be in the same state
		 * as this node device
		 */
		if (jdev_top->nxt_state != jdev->state)
			continue;

		kref_put(&jdev_top->cb_ref, __jesd204_dev_top_state_change_cb);
	}

	return 0;
}

static int jesd204_dev_validate_state_change(struct jesd204_dev *jdev,
					     enum jesd204_dev_state cur_state,
					     enum jesd204_dev_state nxt_state)
{
	if (jdev->state == nxt_state)
		return JESD204_STATE_CHANGE_DONE;

	if (cur_state != jdev->state) {
		dev_warn(jdev->dev, "jesd204 state invalid: %u, should be %u\n",
			 jdev->state, cur_state);
		return jesd204_dev_set_error(jdev, -EINVAL);
	}

	return 0;
}

static int jesd204_dev_run_state_change_cb(struct jesd204_dev *jdev, void *data)
{
	struct jesd204_dev_state_change_data *s = data;
	struct jesd204_dev_top *jdev_top = s->jdev_top;
	int ret;

	ret = jesd204_dev_validate_state_change(jdev,
						jdev_top->jdev.state,
						jdev_top->nxt_state);
	if (ret < 0)
		return ret;

	if (ret == JESD204_STATE_CHANGE_DONE)
		return 0;

	if (s->trigger_state_change_cb) {
		ret = s->trigger_state_change_cb(jdev, s->priv);
		if (ret < 0)
			return ret;
	}

	if (ret != JESD204_STATE_CHANGE_DONE)
		kref_get(&s->jdev_top->cb_ref);

	return 0;
}

static int jesd204_dev_run_state_change(
		struct jesd204_dev *jdev,
		enum jesd204_dev_state cur_state,
		enum jesd204_dev_state nxt_state,
		jesd204_cb_priv trigger_state_change_cb,
		void *update_state_priv,
		jesd204_cb state_complete_cb)
{
	struct jesd204_dev_top *jdev_top = jesd204_dev_top_dev(jdev);
	struct jesd204_dev_state_change_data data;
	int ret;

	ret = jesd204_dev_validate_state_change(jdev, cur_state, nxt_state);
	if (ret < 0)
		return ret;

	if (ret == JESD204_STATE_CHANGE_DONE)
		return 0;

	if (!jdev_top) {
		jdev->state = nxt_state;
		return jesd204_dev_notify_state_change(jdev);
	}

	memset(&data, 0, sizeof(data));
	data.trigger_state_change_cb = trigger_state_change_cb;
	data.priv = update_state_priv;
	data.jdev_top = jdev_top;

	kref_init(&jdev_top->cb_ref);

	jdev_top->state_complete_cb = state_complete_cb;
	jdev_top->nxt_state = nxt_state;

	ret = jesd204_dev_propagate_cb(jdev,
				       jesd204_dev_run_state_change_cb,
				       &data);

	kref_put(&jdev_top->cb_ref, __jesd204_dev_top_state_change_cb);

	return ret;
}

static int jesd204_dev_initialize(struct jesd204_dev *jdev, void *data)
{
	struct jesd204_dev_top *jdev_top = data;
	struct jesd204_dev_list *e;

	e = kzalloc(sizeof(*e), GFP_KERNEL);
	if (!e)
		return -ENOMEM;

	e->jdev = &jdev_top->jdev;
	list_add(&e->list, &jdev->top_devices);

	jdev->state = JESD204_DEV_INITIALIZED;

	return JESD204_STATE_CHANGE_DONE;
}

static int jesd204_of_create_devices(void)
{
	struct jesd204_dev_top *jdev_top;
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

	list_for_each_entry(jdev, &jesd204_device_list, list) {
		ret = jesd204_of_device_create_links(jdev);
		if (ret)
			goto unlock;
	}

	list_for_each_entry(jdev_top, &jesd204_topologies, list) {
		jdev = &jdev_top->jdev;

		ret = jesd204_dev_run_state_change(jdev,
						   JESD204_DEV_UNINITIALIZED,
						   JESD204_DEV_INITIALIZED,
						   jesd204_dev_initialize,
						   jdev_top,
						   NULL);
		if (ret)
			goto unlock;
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

	if (!of_dev_is_jesd204_dev(dev))
		return NULL;

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

static void jesd204_dev_destroy_links(struct jesd204_dev *jdev)
{
	struct jesd204_dev_link *l, *l1;
	struct jesd204_dev_list *e, *e1;
	unsigned int i;

	/* remove this device from the outputs of other devices */
	for (i = 0; i < jdev->inputs_count; i++) {
		l = jdev->inputs[i];
		list_for_each_entry_safe(e, e1, &l->dests, list) {
			list_del(&e->list);
			jesd204_dev_unregister(e->jdev);
			kfree(e);
		}
	}
	kfree(jdev->inputs);
	jdev->inputs_count = 0;

	list_for_each_entry_safe(l, l1, &jdev->outputs, list) {
		list_del(&l->list);
		jesd204_dev_unregister(l->owner);
		kfree(l);
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

	jesd204_dev_destroy_links(jdev);
	kref_put(&jdev->ref, __jesd204_dev_release);
}
EXPORT_SYMBOL(jesd204_dev_unregister);

static void devm_jesd204_dev_unreg(struct device *dev, void *res)
{
	jesd204_dev_unregister(*(struct jesd204_dev **)res);
}

struct jesd204_dev *devm_jesd204_dev_register(struct device *dev,
					      const struct jesd204_dev_data *i)
{
	struct jesd204_dev **jdevp, *jdev;

	if (!of_dev_is_jesd204_dev(dev))
		return NULL;

	jdevp = devres_alloc(devm_jesd204_dev_unreg, sizeof(*jdevp),
			     GFP_KERNEL);
	if (!jdevp)
		return ERR_PTR(-ENOMEM);

	jdev = jesd204_dev_register(dev, i);
	if (!IS_ERR(jdev)) {
		*jdevp = jdev;
		devres_add(dev, jdevp);
	} else {
		devres_free(jdevp);
	}

	return jdev;
}
EXPORT_SYMBOL_GPL(devm_jesd204_dev_register);

static int devm_jesd204_dev_match(struct device *dev, void *res, void *data)
{
	struct jesd204_dev **r = res;

	if (!r || !*r) {
		WARN_ON(!r || !*r);
		return 0;
	}

	return *r == data;
}

/**
 * devm_jesd204_dev_unregister - Resource-managed jesd204_dev_unregister()
 * @dev:	Device this jesd204_dev belongs to
 * @jdev:	the jesd204_dev associated with the device
 *
 * Unregister jesd204_dev registered with devm_jesd204_dev_register().
 */
void devm_jesd204_dev_unregister(struct device *dev, struct jesd204_dev *jdev)
{
	int rc;

	rc = devres_release(dev, devm_jesd204_dev_unreg,
			    devm_jesd204_dev_match, jdev);
	WARN_ON(rc);
}
EXPORT_SYMBOL_GPL(devm_jesd204_dev_unregister);

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

	pr_info("found %u devices and %u topologies\n",
		jesd204_device_count, jesd204_topologies_count);

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
