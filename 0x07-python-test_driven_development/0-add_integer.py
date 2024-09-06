#!/usr/bin/python3
"""
Module to add two integers or floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Args:
        a (int, float): The first number.
        b (int, float, optional): The second number. Defaults to 98.

    Raises:
        TypeError: If either of the arguments is not an integer or float.

    Returns:
        int: The sum of the two numbers, converted to an integer.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
