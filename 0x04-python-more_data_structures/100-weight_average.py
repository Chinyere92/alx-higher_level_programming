#!/usr/bin/python3

def weight_average(my_list=[]):

    to_score = 0
    pep = 0

    if len(my_list) == 0:
        return 0

    for st in my_list:
        to_score += (st[0] * st[1])
        pep += st[1]

    return to_score / pep
