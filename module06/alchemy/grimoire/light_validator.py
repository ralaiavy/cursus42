#!/usr/env/bin/python3

def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    list_ingredients = light_spell_allowed_ingredients()
    for ingredient in list_ingredients:
        if ingredient in ingredients.lower():
            return "VALID"
    return "INVALID"
