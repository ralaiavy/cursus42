#!/usr/bin/env python3
import sys


def parse_inventory() -> dict[str, int]:
    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        parts = arg.split(":")

        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item = parts[0].strip()
        quantity_str = parts[1].strip()
        if item == "":
            print(f"Error - invalid parameter '{item}'")
            continue
        try:
            quantity = int(quantity_str)
        except (ValueError, Exception) as e:
            print(f"Quantity error for '{item}': {e}")
            continue

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        inventory.update({item: quantity})

    return inventory


def display_inventory(inventory: dict[str, int]) -> None:
    print(f"Got inventory: {inventory}")

    items = list(inventory.keys())
    print(f"Item list: {items}")

    total = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total}")

    for item in inventory.keys():
        try:
            percentage = round((inventory[item] / total) * 100, 1)
            print(f"Item {item} represents {percentage}%")
        except ZeroDivisionError as e:
            print(f"error for '{item}': {e}")

    most_item = None
    least_item = None
    max_quantity = 0
    min_quantity = 0

    for item in inventory.keys():
        quantity = inventory[item]

        if most_item is None or quantity > max_quantity:
            most_item = item
            max_quantity = quantity

        if least_item is None or quantity < min_quantity:
            least_item = item
            min_quantity = quantity

    print(
        f"Item most abundant: {most_item} with quantity {max_quantity}"
    )
    print(
        f"Item least abundant: {least_item} with quantity {min_quantity}"
    )


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = parse_inventory()

    if len(inventory) == 0:
        print("At the beginning of the game, your inventory is usually empty")

    else:
        display_inventory(inventory)
        inventory.update({"magic_item": 1})
        print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
