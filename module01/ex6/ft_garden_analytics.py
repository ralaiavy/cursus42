#!/usr/bin/env python3
class Plant:
    class Statistics:
        def __init__(self):
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def grow_called(self) -> None:
            self._grow_calls += 1

        def age_called(self) -> None:
            self._age_calls += 1

        def show_called(self) -> None:
            self._show_calls += 1

        def display(self) -> str:
            return f"Stats: {self._grow_calls} grow, {self._age_calls} age, {self._show_calls} show"

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self._height = 0.0
        self._age = 0
        self._stats = Plant.Statistics()
        self.set_height(height)
        self.set_age(age)

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls, height: float = 0.0, age: int = 0):
        return cls("Unknown", height, age)

    def show(self) -> None:
        self._stats.show_called()
        print(f"{self.name.capitalize()}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self._stats.grow_called()

    def age(self) -> None:
        self._stats.age_called()
        self._age += 20

    def get_stats(self):
        return self._stats

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


    def display_extra_stats(self) -> None:
        pass


class Flower(Plant):

    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self._has_bloomed = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if not self._has_bloomed:
            print(f"{self.name.capitalize()} has not bloomed yet")
        else:
            print(f"{self.name.capitalize()} is blooming beautifully!")

    def bloom(self) -> None:
        self._has_bloomed = True
        
    def grow(self) -> None:
        self._stats.grow_called()
        self._height += 8


class Seed(Flower):

    def __init__(self, name: str, height: float, age: int, color: str, seed_count: int = 0):
        super().__init__(name, height, age, color)
        self.seed_count = seed_count

    def bloom(self) -> None:
        super().bloom()
        self.seed_count = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seed_count}")
        
    def grow(self) -> None:
        self._stats.grow_called()
        self._height += 30


class Tree(Plant):

    def __init__(self, name: str, height: float, age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._shade_calls = 0

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        self._shade_calls += 1
        print(f"Tree {self.name.capitalize()} now produces a shade of {self._height:.1f}cm long and {self.trunk_diameter:.1f}cm wide")

    def get_shade_calls(self) -> int:
        return self._shade_calls
    
    def display_extra_stats(self) -> None:
        print(f"{self._shade_calls} shade")


class Vegetable(Plant):

    def __init__(self, name: str, height: float, age: int, harvest_season: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def grow(self) -> None:
        super().grow()

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1


def display_stats(plant: Plant) -> None:
    stats = plant.get_stats()
    if (plant.name is "Unknown"):
        print(f"[statistics for {plant.name.capitalize()} plant]")
    else:
        print(f"[statistics for {plant.name.capitalize()}]")
    print(stats.display())
    plant.display_extra_stats()


def main() -> None:
    print("=== Garden statistics ===")
    
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print()
    
    print("=== Flower")
    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    display_stats(rose)
    
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_stats(rose)
    print()
    
    print("=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    display_stats(oak)
    
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stats(oak)
    print()
    
    print("=== Seed")
    sunflower = Seed("sunflower", 80.0, 45, "yellow")
    sunflower.show()
    
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age() 
    sunflower.bloom()
    sunflower.show()
    display_stats(sunflower)
    print()
    
    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_stats(anonymous)


if __name__ == "__main__":
    main()