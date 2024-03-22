#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    nbr = 0
    d = 0

    for j in my_list:
        nbr += j[0] * j[1]
        d += j[1]

    return (nbr / d)
