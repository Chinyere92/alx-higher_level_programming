#!/usr/bin/python3

def no_c(my_string):

    strn = []

    for x in my_string:
        if x not in "Cc":
            strn.append(x)
    return " ".join(strn)
