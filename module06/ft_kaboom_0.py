#!/usr/env/bin/python3

from alchemy.grimoire import light_spell_record

if __name__ == "__main__":
    print("Using grimoire module directly")

    res = light_spell_record(
        'Earth, wind and fire', "fire")

    print(
        f"Testing record light spell: {res}"
        )
