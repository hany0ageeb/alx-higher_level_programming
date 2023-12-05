#!/usr/bin/python3
"""This module defines a single function:  pascal_triangle
"""


def right(triangle, row_num, col_num):
    """returns the value above and to right"""
    if row_num == 0:
        return 0
    if col_num >= len(triangle[row_num - 1]):
        return 0
    return triangle[row_num - 1][col_num]


def left(triangle, row_num, col_num):
    """return the value above and to left"""
    if row_num == 0:
        return 0
    if col_num - 1 < 0:
        return 0
    return triangle[row_num - 1][col_num - 1]


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    if n <= 0:
        return []
    triangle = [[1]]
    for row_num in range(1, n):
        triangle.append([])
        for col_num in range(row_num + 1):
            left_val = left(triangle, row_num, col_num)
            right_val = right(triangle, row_num, col_num)
            triangle[row_num].append(right_val + left_val)
    return triangle
