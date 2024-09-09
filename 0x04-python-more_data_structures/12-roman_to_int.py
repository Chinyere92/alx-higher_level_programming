#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rmn = 0
    prev_value = 0

    for curr in roman_string:
        curr_value = roman[curr]

        if curr_value > prev_value:
            rmn += curr_value - 2 * prev_value
        else:
            rmn += curr_value

        # Update previous numeral value
        prev_value = curr_value

    return rmn
