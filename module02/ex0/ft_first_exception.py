#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()
    try:
        temperature = input_temperature("25")
        print(f"Temperature is now {temperature}°C")
        print()
    except (ValueError, TypeError) as e:
        print(f"Caught input_temperature error: {e}")

    try:
        temperature = input_temperature("abc")
        print(f"Temperature is now {temperature}°C")
    except (ValueError, TypeError) as e:
        print(f"Caught input_temperature error: {e}")
        print()

    print("All tests completed - program didn't crash!")


def main() -> None:
    test_temperature()


if __name__ == "__main__":
    main()
