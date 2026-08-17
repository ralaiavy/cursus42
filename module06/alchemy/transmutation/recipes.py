#!/usr/env/bin/python3

from elements import create_fire
from ..elements import create_air
from ..potions import strength_potion


def lead_to_gold() -> str:
    result = f"Recipe transmuting Lead to Gold: brew '{create_air()}'"
    result_next = f" and '{strength_potion()}' mixed with '{create_fire()}'"
    return result + result_next
