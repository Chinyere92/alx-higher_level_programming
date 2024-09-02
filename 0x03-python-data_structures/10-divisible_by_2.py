#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    if my_list is None or len(my_list) == 0:
        return None

    new = []
    for x in my_list:
        if x % 2 == 0:
            new.append(True)
        else:
            new.append(False)
    return new
