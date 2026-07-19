#!/usr/bin/env python3
class Plant:

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"Plant: {self.name.capitalize()}")
        print(f"Height: {self.height}cm")
        print(f"Age: {self.age} days")
        print("-" * 20)


def main() -> None:
    plant1 = Plant("rose", 25.0, 30)
    plant2 = Plant("oak", 200.0, 365)
    plant3 = Plant("cactus", 15.0, 90)

    print("=== Garden Plant Registry ===")
    plant1.show()
    plant2.show()
    plant3.show()


if __name__ == "__main__":
    main()
