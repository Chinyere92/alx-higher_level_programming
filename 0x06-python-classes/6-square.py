#!/usr/bin/python3
"""
Module with Square class.
"""


class Square:
    """
    Declaration:
        Declaration of class Square with
        a private variable `size` and `position`.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialization method:
        - Optionally initializes the square with a given size.
        - Includes value and type checks for size and position.
        - Private instance attribute: position
        - Position must be a tuple of 2 positive integers.
        - Raises a TypeError if conditions are not met.
        """
        self.size = size  # Using the setter to initialize the size with checks
        self.position = position

    @property
    def position(self):
        """
        Position:
            - Getter for position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Position setter:
            - Validates that position is a tuple of 2 positive integers.
            - Raises TypeError if validation fails.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            - Prints the square with the character '#'.
            - Uses spaces for horizontal positioning.
            - Skips lines for vertical positioning when position[1] > 0.
            - If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        # Print vertical spaces
        print("\n" * self.__position[1], end="")

        # Print the square
        for i in range(self.__size):
            print(" " * self.__position[0], end="")  # Horizontal position
            print("#" * self.__size)

    def area(self):
        """
        Public Method:
        - Calculates and returns the area of the square.
        """
        return self.__size ** 2
