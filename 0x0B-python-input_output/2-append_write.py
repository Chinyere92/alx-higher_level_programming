#!/usr/bin/python3
"""
A function that appends a string at the end of a text file (UTF8)
And returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    FUNCTION:
        - If the file doesn’t exist, it should be created
        - Must use the with statement
        - don’t need to manage file permision or file doesn't exist exceptions.
    """

    with open(filename, "a") as file:
        return file.write(text)
