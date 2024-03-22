#!/usr/bin/python3

def roman_to_int(roman_string):
    rmns = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if (roman_string is None) or (type(roman_string) is not str):
        return 0

    nbr = len(roman_string)
    val_int = rmns[roman_string[number-1]]
    for j in range(nbr - 1, 0, -1):
        current_val = rmns[roman_string[j]]
        previous_val = rmns[roman_string[j-1]]

        if previous_val >= current_val:
            val_int += previous_val
        else:
            val_int -= previous_val

    return val_int
