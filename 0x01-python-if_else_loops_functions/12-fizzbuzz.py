#!/usr/bin/python3
def fizzbuzz():
    for nb in range(1, 101):
        if nb % 3 == 0 and nb % 5 == 0:
            print("FizzBuzz ", end="")
        elif nb % 3 == 0:
            print("Fizz ", end="")
        elif nb % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(nb), end="")
