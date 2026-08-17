#!/usr/env/bin/python3


if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directy")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

    import alchemy.grimoire.dark_spellbook

    res = alchemy.grimoire.dark_spellbook.dark_spell_record(
                'Earth, wind and fire', "fire")
    print(f"Testing record light spell: {res}")
