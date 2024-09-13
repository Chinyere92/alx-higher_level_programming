#!/usr/bin/python3
"""
Class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square:
    - Inherits from Rectangle
    - Uses width and height from Rectangle but ensures they are always equal
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance.
        Args:
            size (int): The size of the square (equal to both width and height)
            x (int): The x position of the square
            y (int): The y position of the square
            id (int): Optional id value
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Overloads the __str__ method to return:
        [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Getter for size (which is the same as width/height)
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size, assigns the same value to both width and height
        """
        self.width = value
        self.height = value
