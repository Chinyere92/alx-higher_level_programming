#!/usr/bin/python3
"""
Module that defines a Square class with comparison based on area.
"""


class Square:
    """
    Class Square:
        - Defines a square with a private attribute `size`.
        - Supports comparison based on the square's area.
    """

    def __init__(self, size=0):
        """
        Initialization method:
        - Instantiates the square with a size.
        - Uses the property setter to validate size.
        """
        self.size = size

    @property
    def size(self):
        """
        Size property:
            - Retrieves the current value of size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Size setter:
            - Validates that size is a number (int or float).
            - Raises a TypeError if size is not a number.
            - Raises a ValueError if size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Public method to calculate the square's area.
        - Returns the area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Equality comparison (==) based on the square's area.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Inequality comparison (!=) based on the square's area.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Less than comparison (<) based on the square's area.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal comparison (<=) based on the square's area.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Greater than comparison (>) based on the square's area.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater than or equal comparison (>=) based on the square's area.
        """
        return self.area() >= other.area()
