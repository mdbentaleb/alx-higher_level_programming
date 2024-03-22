#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    for k, vl in sorted(a_dictionary.items()):
        if vl == value:
            del a_dictionary[k]
    return a_dictionary
