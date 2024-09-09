#!/usr/bin/python3

def roman_to_int(roman_string):

    rmn = 0

    if roman_string is None or not isinstance(roman_string, str):
        return rmn

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev = roman_string[0]

    for curr in roman_string:

        if roman[curr] == roman[prev]:
            rmn += roman[curr]
            prev = curr
        elif roman[curr] > roman[prev]:
            rmn = (roman[curr] - rmn) - 2
            prev = curr
        else:
            rmn += roman[curr]
            prev = curr
    return rmn
