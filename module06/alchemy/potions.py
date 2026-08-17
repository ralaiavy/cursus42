#!/user/env/bin/python3

from .elements import create_air, create_earth
from elements import create_fire, create_water


def healing_potion() -> str:
    result = f"Healing potion brewed with '{create_earth()}' "
    next_result = f"and '{create_air()}'"
    return result + next_result


def strength_potion() -> str:
    result = f"Strength potion brewed with ’{create_fire()}’ "
    next_result = f"and ’{create_water()}"
    return result + next_result
