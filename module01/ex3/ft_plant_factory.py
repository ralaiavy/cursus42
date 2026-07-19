#!/usr/bin/env python3
class Plant:

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"Created: {self.name.capitalize()}:"
              f"{self.height:.1f}cm, {self.age} days old")

    def grow(self) -> None:
        self.height += 0.8

    def ages(self) -> None:
        self.age += 1


def main() -> None:
    plants = [
        Plant("rose", 25.0, 30),
        Plant("oak", 200.0, 365),
        Plant("cactus", 5.0, 90),
        Plant("sunflower", 80.0, 45),
        Plant("fern", 15.0, 120),
    ]

    print("Plant Factory Output")
    for plant in plants:
        plant.show()


if __name__ == "__main__":
    main()
