#!/usr/bin/env python3
def garden_operations(operation_number: int) -> str:
    if operation_number == 0:
        int("abc")
        return "Never reached"

    elif operation_number == 1:
        result = 10 / 0
        return f"Never reached: {result}"

    elif operation_number == 2:
        open("/non/existent/file", "r")
        return "Never reached"

    elif operation_number == 3:
        result = "Temperature: " + 42
        return f"Never reached: {result}"

    else:
        return "Operation completed successfully"


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for i in [0, 1, 2, 3, 4]:
        print(f"Testing operation {i}...")
        try:
            result = garden_operations(i)
            print(result)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
    print()
    print("All error types tested successfully!")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
