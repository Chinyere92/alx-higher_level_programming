#!/usr/bin/python3
"""
A function that returns an object (Python data structure)
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Function:
        - Returns an object (Python data structure)
        - Don’t need to manage exceptions if the JSON string doesn’t represent
    """
    return json.loads(my_str)
