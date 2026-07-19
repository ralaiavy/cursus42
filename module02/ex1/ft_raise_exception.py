#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)
    print(f"Input data is '{temp_str}'")

    if temperature < 0:
        raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")
    elif temperature > 40:
        raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")

    return temperature


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print()
    try:
        temperature = input_temperature("25")
        print(f"Temperature is now {temperature}°C")
    except (ValueError, TypeError) as e:
        print(f"Caught input_temperature error: {e}")
    print()
    try:
        temperature = input_temperature("abc")
        print(f"Temperature is now {temperature}°C")
    except (ValueError, TypeError) as e:
        print(f"Caught input_temperature error: {e}")
    print()
    try:
        temperature = input_temperature("100")
        print(f"Temperature is now {temperature}°C")
    except (ValueError, TypeError) as e:
        print(f"Caught input_temperature error: {e}")
    print()
    try:
        temperature = input_temperature("-50")
        print(f"Temperature is now {temperature}°C")
    except (ValueError, TypeError) as e:
        print(f"Caught input_temperature error: {e}")
    print()
    print("All tests completed - program didn't crash!")


def main() -> None:
    test_temperature()


if __name__ == "__main__":
    main()
