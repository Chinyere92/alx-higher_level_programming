#!/usr/bin/python3
"""
Class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle:
    - Inherits from Base
    - Private instance attributes with public getters and setters
    - Includes validation for setters
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        width property to return width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter set value after checking conditions
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """
        height property to return height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter to set height after condition is verified
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """
        property x to return x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter to set value to x after checking conditions
        """
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """
        property y to return value y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        To set value y after conditions are checked
        """
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """
        return the area of reactangle
        """
        return self.__width * self.__height
