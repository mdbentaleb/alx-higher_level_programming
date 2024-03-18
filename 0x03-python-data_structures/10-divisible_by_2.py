#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    nwlist = []
    for j in range(len(my_list)):
        if my_list[j] % 2 == 0:
            nwlist.append(True)
        else:
            nwlist.append(False)

    return nwlist
