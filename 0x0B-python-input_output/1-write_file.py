#!/usr/bin/python3
"""
A function that writes a string to a text file (UTF8)
And returns the number of characters written
"""


def write_file(filename="", text="", encoding="utf-8"):

    """
    FUNCTION:
        - create the file if doesn’t exist.
        - Don’t need to manage file permission exceptions.
        - Overwrite the content of the file if it already exists.
    """
    with open(filename, "w") as file:
        return file.write(text)
