#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":

    lst = dir(hidden_4)

    for x in range(len(lst)):

        if lst[x][0] != '_':
            print(lst[x])
