#!/usr/bin/python3
for nbr1 in range(0, 10):
    for nbr2 in range(nbr1 + 1, 10):
        if nbr1 == 8 and nbr2 == 9:
            print("{}{}".format(nbr1, nbr2))
        else:
            print("{}{}".format(nbr1, nbr2), end=", ")
