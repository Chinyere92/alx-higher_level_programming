#!/usr/bin/python3
"""
A script that adds all arguments to a Python list and saves them to a file
"""
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item():
    """
    FUNCTION:
        - Adds all command-line arguments to a Python list.
        - Loads the existing list from 'add_item.json' if the file exists.
        - Saves the updated list back to 'add_item.json' using JSON repr
        - Uses save_to_json_file and load_from_json_file functions.
        - If the file doesn’t exist, it will be created.
    """
    filename = "add_item.json"

    if os.path.exists(filename):
        lists = load_from_json_file(filename)
    else:
        lists = []

    lists.extend(sys.argv[1:])

    save_to_json_file(lists, filename)


add_item()
