#!/usr/bin/python3

def max_integer(my_list=[]):

    mx = 0

    if my_list is None or len(my_list) == 0:
        return None

    for x in my_list:
        if x > mx:
            mx = x

    return mx
