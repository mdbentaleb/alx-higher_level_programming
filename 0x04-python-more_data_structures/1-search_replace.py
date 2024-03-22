#!/usr/bin/python3

def search_replace(my_list, search, replace):
    nw_lst = my_list[:]
    for j in range(len(nw_lst)):
        if nw_lst[j] == search:
            nw_lst[j] = replace
    return nw_lst
