#!/usr/bin/env python3
import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        args_count = len(sys.argv) - 1
        print(f"Arguments received: {args_count}")

        i = 1
        while (i < len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1

    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
