#!/usr/bin/python3
"""
Module with square class
"""


class Square:
    """
    Declaration:
        Declaration of class Square with
        a private variable `size`.
    """

    def __init__(self, size=0):
        """
        Initialization method:
        - Optionally initializes the square with a given size.
        - Includes value and type checks.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):

        """
        Public Method:
        - Public method Area
        - Return Sqr area
        """
        return self.__size ** 2
