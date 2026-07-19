#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age
        self.growth_rate = 0.8

    def show(self) -> None:
        print(f"{self.name.capitalize()}:"
              f" {self.height:.1f}cm, {self.age} days old")

    def grow(self) -> None:
        self.height += self.growth_rate

    def years(self) -> None:
        self.age += 1


def main() -> None:
    plant = Plant("rose", 25.0, 30)
    initial_height = plant.height

    print("== Garden Plant Growth ==")
    plant.show()

    for day in range(1, 8):
        plant.grow()
        plant.years()
        print(f"== Day {day} ==")
        plant.show()
    growth = plant.height - initial_height
    print(f"Growth this week: {growth:.1f}cm")


if __name__ == "__main__":
    main()
