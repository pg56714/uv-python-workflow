"""
Entry point demonstrating usage of the calculator module.

Runs a simple example that prints the result of adding two numbers using the
``src.calculator`` module.
"""

from src.calculator import add


def main() -> None:
    """Run the example and print a simple addition result."""

    result = add(1, 2)
    print(f"Example: 1 + 2 = {result}")


if __name__ == "__main__":
    main()
