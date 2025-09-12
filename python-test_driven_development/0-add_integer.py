#!/usr/bin/python3
"""
This module provides a single function, add_integer(a, b=98),
which returns the integer addition of two numbers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.

    Parameters:
        a (int or float): The first number to add.
        b (int or float, optional): The second number to add. Defaults to 98.

    Returns:
        int: The result of the addition of a and b, both casted to integers.

    Raises:
        TypeError: If a or b are not integers or floats.
        OverflowError: If a or b is float('inf').

    Notes:
        - Floats are first casted to integers (truncated, not rounded).
        - float('inf') is considered invalid and raises an OverflowError.
        - Python integers have arbitrary precision, so there's 
          no integer overflow.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a == float('inf') or b == float('inf'):
        raise OverflowError("Cannot add infinity")
    return int(a) + int(b)
