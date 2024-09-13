#!/usr/bin/python3
"""
The “base” of all other classes in this project.
"""


class Base:
    """
    Class Base for base project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor:
        - If id is provided (not None), set it as the public instance attr
        - If id is not provided, incr __nb_objects and assign the new value
        - to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
