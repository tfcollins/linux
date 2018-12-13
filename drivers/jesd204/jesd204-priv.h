/**
 * The JESD204 framework
 *
 * Copyright (c) 2019 Analog Devices Inc.
 *
 * This program is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License version 2 as published by
 * the Free Software Foundation.
 */

#ifndef _JESD204_PRIV_H_
#define _JESD204_PRIV_H_

#include <linux/jesd204/jesd204.h>

struct jesd204_dev;
struct jesd204_dev_top;

enum jesd204_dev_state {
	JESD204_DEV_UNINITIALIZED = 0,
	JESD204_DEV_INITIALIZED,
	JESD204_DEV_PROBED,
	JESD204_DEV_CLOCKS_READY,
};

typedef int (*jesd204_cb)(struct jesd204_dev *jdev);
typedef int (*jesd204_cb_priv)(struct jesd204_dev *jdev, void *data); 

/**
 * struct jesd204_dev_list - Entry for a JESD204 device in a list
 * @list		list entry for a device to keep a list of links
 * @jdev		pointer to JESD204 device for this list entry
 */
struct jesd204_dev_list {
	struct list_head		list;
	struct jesd204_dev		*jdev;
};

/**
 * struct jesd204_dev_link - Entry for a JESD204 device link
 * @list		list entry for a device to keep a list of links
 * @owner		pointer to JESD204 device to which this link belongs to
 * @dests		list of JESD204 devices this link is connected as input
 * @of			device-tree reference and arguments for this link
 */
struct jesd204_dev_link {
	struct list_head		list;
	struct jesd204_dev		*owner;
	struct list_head		dests;
	struct of_phandle_args		of;
};

/**
 * struct jesd204_dev - JESD204 device
 * @list		list entry for the framework to keep a list of devices
 * @is_top		true if this device is a top device in a JESD204
 *			topology
 * @top_devices		list of top devices that this device is connected to
 * @dev			device that registers itself as a JESD204 device
 * @ops			JESD204 operations specified via function pointers
 * @np			reference in the device-tree for this JESD204 device
 * @ref			ref count for this JESD204 device
 * @inputs		array of pointers to output links from other devices
 * @outputs		list of JESD204 output links devices that take input from this device
 * @error		error code of the last operation/state transition
 * @state		current state of this JESD204 device
 */
struct jesd204_dev {
	struct list_head		list;

	bool				is_top;
	struct list_head		top_devices;

	struct device			*dev;
	struct jesd204_dev_ops		*ops;
	struct device_node		*np;
	struct kref			ref;

	struct jesd204_dev_link		**inputs;
	uint32_t			inputs_count;
	struct list_head		outputs;

	int				error;
	enum jesd204_dev_state		state;
};

/**
 * struct jesd204_dev_top - JESD204 top device (in a JESD204 topology)
 * @list		list entry for the framework to keep a list of top
 *			devices (and implicitly topologies)
 * @jdev		JESD204 device data
 * @state_complete_cb	callback that gets called after a topology has finished
 *			it's state transition, meaning that all JESD204 devices
 *			have moved to the desired @nxt_state
 * @cb_ref		kref which all JESD204 devices will increment when they
 *			need to defer their state transition; an equivalent
 *			notification must be called by the device to decrement
 *			this and finally call the @state_complete_cb
 *			callback (if provided)
 * @nxt_state		next state this topology has to transition to
 * @error		true if there was an error in the last topology
 *			transition
 */
struct jesd204_dev_top {
	struct list_head		list;

	struct jesd204_dev		jdev;

	jesd204_cb			state_complete_cb;
	struct kref			cb_ref;
	enum jesd204_dev_state		nxt_state;

	bool				error;
};

/**
 * struct jesd204_dev_state_change_data - JESD204 device state change data
 * @jdev_top			top JESD204 for which this state change
 * @trigger_state_change_cb	callback to propagate to trigger state change
 * @priv			private data for @trigger_state_change_cb
 */ 
struct jesd204_dev_state_change_data {
	struct jesd204_dev_top	*jdev_top;
	jesd204_cb_priv		trigger_state_change_cb;
	void			*priv;
};

static inline struct jesd204_dev_top *jesd204_dev_top_dev(
		struct jesd204_dev *jdev)
{
	if (!jdev || !jdev->is_top)
		return NULL;
	return container_of(jdev, struct jesd204_dev_top, jdev);
}

static inline bool of_dev_is_jesd204_dev(struct device *dev)
{
	if (!dev || !dev->of_node)
		return false;
	return of_property_read_bool(dev->of_node, "jesd204-device");
}

#endif /* _JESD204_PRIV_H_ */
