#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":

    total = 0

    for x in range((len(argv) - 1)):

        total += int(argv[1 + x])
    print(total)
