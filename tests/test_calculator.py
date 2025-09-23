"""Tests for calculator arithmetic functions."""

import math

import pytest

from src.calculator import add, divide, multiply, subtract


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
