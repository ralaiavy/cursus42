#!/user/env/bin/python3

import alchemy


if __name__ == "__main__":
    print("=== Alembic 4 ===")
    try:
        print("Accessing the alchemy module using 'import alchemy'")
        print(f"Testing create_air: {alchemy.create_air()}")
        print("Now show that not all functions can be reached")
        print("This will raise an exception!")
        print(f"{alchemy.create_earth()}")
    except Exception as e:
        print(f"Got exception: {e}")
