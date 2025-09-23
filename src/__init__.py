"""
Public API for the calculator example package.

This module re-exports arithmetic functions for convenient imports:
``from src import add, subtract, multiply, divide``.
"""

from .calculator import add, divide, multiply, subtract

__all__ = ["add", "subtract", "multiply", "divide"]
