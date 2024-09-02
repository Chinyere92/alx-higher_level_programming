#!/usr/bin/python3

def delete_at(my_li=[], idx=0):

    if my_li is None or len(my_li) == 0 or idx > (len(my_li) - 1) or idx < 0:
        return my_list

    del my_li[idx]
    return my_li
