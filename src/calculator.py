# Enable postponed evaluation of type annotations (PEP 563)
"""
Calculator module providing basic arithmetic functions.

This module exposes four operations: addition, subtraction, multiplication, and
division. All functions accept integers or floats and return the corresponding
numeric result. Division by zero raises ``ZeroDivisionError``.
"""

from __future__ import annotations

Number = int | float


def add(a: Number, b: Number) -> Number:
    """Return the sum of ``a`` and ``b``."""

    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return the difference of ``a`` minus ``b``."""

    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return the product of ``a`` and ``b``."""

    return a * b


def divide(a: Number, b: Number) -> Number:
    """
    Return the quotient of ``a`` divided by ``b``.

    Raises
    ------
    ZeroDivisionError
        If ``b`` equals 0.
    """

    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def power(base: Number, exponent: Number) -> Number:
    """
    Return ``base`` raised to the power of ``exponent``.

    Supports integers and floats. For fractional exponents of negative bases,
    Python will return a complex number; since this module is typed for
    real numbers, such usage is not supported and will raise ``ValueError``.
    """

    # Disallow fractional exponent for negative base to keep return type real
    if isinstance(base, (int, float)) and isinstance(exponent, (int, float)):
        if base < 0 and not float(exponent).is_integer():
            raise ValueError("fractional power of a negative base is not a real number")
    return base**exponent
