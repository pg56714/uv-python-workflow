"""Tests for calculator arithmetic functions."""

import math

import pytest

from src.calculator import add, divide, multiply, power, subtract


def test_add() -> None:
    """add returns correct sums for ints and floats."""
    assert add(1, 2) == 3
    assert add(1.5, 2.5) == 4.0


def test_subtract() -> None:
    """subtract returns correct differences for ints and floats."""
    assert subtract(5, 3) == 2
    assert subtract(5.5, 0.5) == 5.0


def test_multiply() -> None:
    """multiply returns correct products for ints and floats."""
    assert multiply(4, 3) == 12
    assert multiply(2.5, 2) == 5.0


def test_divide() -> None:
    """divide returns correct quotients for ints and floats."""
    assert divide(10, 2) == 5
    assert math.isclose(divide(7, 2), 3.5)


def test_divide_by_zero() -> None:
    """divide raises ZeroDivisionError when dividing by zero."""
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_power_integers() -> None:
    """power returns correct results for integer base and exponent."""
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(-2, 4) == 16
    assert power(-2, 3) == -8


def test_power_floats() -> None:
    """power returns correct results for float exponents where applicable."""
    assert math.isclose(power(9, 0.5), 3.0)
    assert math.isclose(power(16.0, 0.25), 2.0)


def test_power_invalid_fractional_negative_base() -> None:
    """power raises ValueError for fractional exponent on negative base (non-real)."""
    with pytest.raises(ValueError):
        power(-8, 1 / 3)
