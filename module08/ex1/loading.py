import importlib
import sys
from typing import Any

DEPENDENCIES = [
    "pandas",
    "numpy",
    "matplotlib",
]


def check_dependencies() -> bool:
    success = True

    print("Checking dependencies...\n")

    for module_name in DEPENDENCIES:
        try:
            module = importlib.import_module(module_name)
            print(f"[OK] {module_name} ({module.__version__})")
        except ImportError:
            success = False
            print(f"[MISSING] {module_name}")

    return success


def show_package_manager_comparison() -> None:

    print("\n\tpip:")
    print("  - Installs packages from requirements.txt")
    print("  - Virtual environment created manually")
    print("  - No lock file by default")

    print("\n\tPoetry:")
    print("  - Installs packages from pyproject.toml")
    print("  - Creates and manages a virtual environment")
    print("  - Generates poetry.lock for reproducible installs")


def analyze_matrix_data(pd: Any, np: Any, plt: Any) -> None:
    print("\nAnalyzing Matrix data...")

    data = np.random.normal(loc=50, scale=10, size=1000)

    print("Processing 1000 data points...")

    df = pd.DataFrame({"Matrix Signal": data})

    print("Generating visualization...")

    plt.figure(figsize=(8, 5))
    plt.plot(df.index, df["Matrix Signal"])
    plt.title("Matrix Data Analysis")
    plt.xlabel("Sample")
    plt.ylabel("Signal")
    plt.grid(True)

    plt.savefig("matrix_analysis.png")
    plt.close()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")

    if not check_dependencies():
        show_package_manager_comparison()
        print("\nTo install the missing packages:\n")
        print("Using pip:")
        print("    pip install -r requirements.txt\n")
        print("Using Poetry:")
        print("    poetry install\n")
        print("Program terminated.")
        sys.exit(1)

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    show_package_manager_comparison()
    print("\nAll dependencies are available!")
    print(f"pandas version     : {pd.__version__}")
    print(f"numpy version      : {np.__version__}")
    print(f"matplotlib version : {plt.matplotlib.__version__}")

    analyze_matrix_data(pd, np, plt)


if __name__ == "__main__":
    main()
