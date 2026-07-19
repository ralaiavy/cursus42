#!/usr/bin/env python3
class GardenError(Exception):

    def __init__(self, message: str = "Unknown garden error occurred"):
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):

    def __init__(self, message: str = "Unknown plant error occurred"):
        self.message = message
        super().__init__(self.message)


class WaterError(GardenError):

    def __init__(self, message: str = "Unknown watering error occurred"):

        self.message = message
        super().__init__(self.message)


def test_plant_problem(d: int, s: str) -> None:
    if (d > 1):
        raise PlantError(f"The {s} plant is wilting!")


def test_water_problem(d: int) -> None:
    if (d > 1):
        raise WaterError("Not enough water in the tank!")


def test_garden_problem() -> None:

    raise GardenError()


def test_error_types() -> None:

    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        test_plant_problem(2, "Tomato")
    except (PlantError, Exception) as e:
        print(f"Caught PlantError: {e}")
    print()
    print("Testing WaterError...")
    try:
        test_water_problem(2)
    except (WaterError, Exception) as e:
        print(f"Caught WaterError: {e}")
    print()
    print("Testing catching all garden errors...")

    try:
        test_plant_problem(2, "Tomato")
    except (GardenError, Exception) as e:
        print(f"Caught GardenError: {e}")

    try:
        test_water_problem(2)
    except (GardenError, Exception) as e:
        print(f"Caught GardenError: {e}")
        print()

    print("All custom error types work correctly!")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
