#!/usr/bin/env python3
class Plant:

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def show(self) -> None:
        print(f"{self.name.capitalize()}:"
              f" {self._height:.1f}cm, {self._age} days old")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height < 0:
            print("Error, height can't be negative")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print("Error, age can't be negative")
        else:
            self._age = age


def main() -> None:
    print("=== Garden Security System ===")

    plant = Plant("rose", 15.0, 10)
    print("Plant created:", end=" ")
    plant.show()
    print()

    plant.set_height(25.0)
    plant.set_age(30)
    print("Height updated: 25cm")
    print("Age updated: 30 days")
    print()

    print("Rose:", end=" ")
    plant.set_height(-5.0)
    print("Height update rejected")

    print("Rose:", end=" ")
    plant.set_age(-10)
    print("Age update rejected")
    print()

    print("Current state:", end=" ")
    plant.show()


if __name__ == "__main__":
    main()
