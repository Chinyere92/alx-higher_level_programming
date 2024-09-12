#!/usr/bin/python3
"""
A function that returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean) for JSON
serialization of an object
"""
def class_to_json(obj):
    """
    FUNCTION:
        - Function that returns the dictionary description with simple data
          structure
        - obj is an instance of a Class
        - Attributes of the obj Class are serializable
    """
    return obj.__dict__
