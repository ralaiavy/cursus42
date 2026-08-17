#!/usr/env/bin/python3

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    list_ingredients = dark_spell_allowed_ingredients()
    for ingredient in list_ingredients:
        if ingredient in ingredients.lower():
            return "VALID"
    return "INVALID"
