#!/usr/bin/python3
"""MyList class module"""


class MyList(list):
    """Custom MyList"""
    def print_sorted(self):
        """printing sorted list"""
        print(sorted(self))
