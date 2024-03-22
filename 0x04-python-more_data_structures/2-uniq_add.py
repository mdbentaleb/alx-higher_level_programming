#!/usr/bin/python3

def uniq_add(my_list=[]):
    res = 0
    for j in set(my_list):
        res += j
    return res
