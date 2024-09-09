#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    n_dict = a_dictionary.copy()

    for x in n_dict:
        n_dict[x] = n_dict[x] * 2

    return n_dict
