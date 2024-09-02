#!/usr/bin/python3

def no_c(my_string):

    my_copy = []

    for x in my_string:
        if x not in "Cc":
            my_copy.append(x)
    return "".join(my_copy)
