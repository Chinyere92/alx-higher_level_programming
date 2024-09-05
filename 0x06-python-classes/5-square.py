#!/usr/bin/python3
"""
Module with Square class.
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
        self.size = size  # Using the setter to initialize the size with checks

    @property
    def size(self):
        """
        Property method:
            - Returns the current value of the size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter of size:
            - Checks if the value is an integer.
            - Raises TypeError if the value is not an integer.
            - Checks if the value is >= 0.
            - Raises ValueError if the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        My_print Method:
            - prints in stdout the square with the character #
            - if size is equal to 0, print an empty line
        """
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            print("#" * self.__size)

    def area(self):
        """
        Public Method:
        - Calculates and returns the area of the square.
        """
        return self.__size ** 2
