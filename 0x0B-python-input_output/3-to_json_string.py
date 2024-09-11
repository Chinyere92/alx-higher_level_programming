#!/usr/bin/python3
"""
A function that returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """
    Function:
    - don’t need to manage exceptions if the object can’t be serialized.
    - JSON representation of an object
    """
    return json.dumps(my_obj)
