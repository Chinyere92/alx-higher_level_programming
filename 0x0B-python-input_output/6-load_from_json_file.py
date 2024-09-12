#!/usr/bin/python3
"""
A function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    FUNCTION:
        - Creates an Object from a “JSON file.”
        - Uses the 'with' statement for proper file handling.
        - No need to manage exception if JSON content doesn't represent an obj.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
