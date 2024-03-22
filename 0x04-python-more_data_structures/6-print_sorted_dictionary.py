#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for k, val in sorted(a_dictionary.items()):
        print(k, val, sep=': ')
