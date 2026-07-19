#!/usr/bin/env python3
class Plant:

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self._height:.1f}cm,"
              f" {self._age} days old")

    def grow(self) -> None:
        self._height += 2.1

    def age(self) -> None:
        self._age += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"Error, height can't be negative: {height}")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Error, age can't be negative: {age}")
        else:
            self._age = age


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self._has_bloomed = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if (self._has_bloomed is False):
            print("Rose has not bloomed yet")
        else:
            print(f"{self.name.capitalize()} is blooming beautifully!")

    def bloom(self) -> None:
        self._has_bloomed = True


class Tree(Plant):

    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self.name.capitalize()}"
              f" now produces a shade of {self._height}cm long and"
              f"{self.trunk_diameter:.1f}cm wide")


class Vegetable(Plant):

    def __init__(self, name: str, height: float,
                 age: int, harvest_season: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f"  Harvest season: {self.harvest_season}")
        print(f"  Nutritional value: {self.nutritional_value}")

    def grow(self) -> None:
        super().grow()

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1


def main() -> None:
    print("=== Garden Plant Types ===")

    rose = Flower("rose", 15.0, 10, "red")
    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")

    rose = Flower("rose", 15.0, 10, "red")
    rose.bloom()
    rose.show()
    print()

    oak = Tree("oak", 200.0, 365, 5)
    print("=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    tomato = Vegetable("tomato", 5.0, 10, "April")
    print("=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")

    for i in range(20):
        tomato.grow()

    for i in range(20):
        tomato.age()

    tomato.show()


if __name__ == "__main__":
    main()
