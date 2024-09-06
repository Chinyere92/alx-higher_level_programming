#!/usr/bin/python3
"""
Magic class
"""
import math


class MagicClass:
    """
    Class MagicClass that mimics the provided bytecode.
    """

    def __init__(self, radius=0):
        """
        Initialization method:
        - Validates the radius to be either an integer or float.
        - If not, raises a TypeError.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Method that calculates the area of the circle:
        - Uses the formula: area = π * radius^2
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """
        Method that calculates the circumference of the circle:
        - Uses the formula: circumference = 2 * π * radius
        """
        return 2 * math.pi * self.__radius
