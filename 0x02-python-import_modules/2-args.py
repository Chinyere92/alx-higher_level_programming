#!/usr/bin/python3

"""
print the list of argument passed
"""
from sys import argv

if __name__ == "__main__":

    t_len = len(argv) - 1

    if t_len == 0:
        print("{:d} arguments.".format(t_len))
    elif t_len == 1:
        print("{:d} argument:".format(t_len))
    else:
        print("{:d} arguments:".format(t_len))

    for x in range(t_len):
        print("{:d}: {}".format(x + 1, argv[x+1]))
