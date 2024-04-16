#!/usr/bin/python3
"""def pascal_triangle"""


def pascal_triangle(n):
    """
        returns a list of lists of integers
        Args:
            n(int): to be repped
    """
    triangle = []
    inner_list  = []
    if not n <= 0:
        for j in range(n):
            innerlist.append(j + 1)
            triangle.append(inner_list)
    return triangle
