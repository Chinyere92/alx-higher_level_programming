#!/usr/bin/python3
"""
Function that writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function:
        - Writes an Object to a text file, using a JSON representation
        - Must use the with statement
        - Don’t need to manage exceptions if the object can’t be serialized.
    """
    with open(filename, "w") as file:
        return json.dump(my_obj, file)
