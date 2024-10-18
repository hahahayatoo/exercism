"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    result = {}
    for item in items:
        if "not found" == result.get(item, "not found"):
            result[item] = 1
        else:
            result[item] += 1

    return result


def add_items(inventory: dict, items: list):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for item in items:
        if "not found" == inventory.get(item, "not found"):
            inventory[item] = 1
        else:
            inventory[item] += 1

    return inventory


def decrement_items(inventory: dict, items: list):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for item in items:
        if "not found" != inventory.get(item, "not found") and inventory[item] > 0:
            inventory[item] -= 1

    return inventory


def remove_item(inventory: dict, item: list):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if "not found" != inventory.get(item, "not found"):
        inventory.pop(item)

    return inventory


def list_inventory(inventory: dict):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    results = []
    for key, value in inventory.items():
        if value > 0:
            results.append((key, value))

    return results
