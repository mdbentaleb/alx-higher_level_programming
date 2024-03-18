#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    else:
        mx = my_list[0]
        for j in range(len(my_list)):
            if my_list[j] > mx:
                mx = my_list[j]

        return mx
