#!/usr/bin/python3

"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """Print Pascal's Triangle
    Args:
        n (int): Size of the pascal triangle
    """
    res = []
    if (n <= 0):
        return res
    else:
        for x in range(n+1):
            temp = []
            c = 1
            for y in range(1, x+1):
                temp.append(c)
                c = c * (x - y) // y
            if (len(temp)):
                res.append(temp)
    return res
