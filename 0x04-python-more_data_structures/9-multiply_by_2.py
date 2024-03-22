#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    nw_dct = {j: (a_dictionary[j] * 2) for j in a_dictionary}
    return nw_dct
