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
