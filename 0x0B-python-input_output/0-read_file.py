#!/usr/bin/python3
"""
A function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):

    """
    READFILE:
        - Opens and reads the content of a UTF-8 text file.
        - Uses the 'with' statement for automatic file closing.
        - Does not handle exceptions explicitly.
    """

    with open(filename, 'r') as file:
        rd = file.read()
    print(rd, end='')
