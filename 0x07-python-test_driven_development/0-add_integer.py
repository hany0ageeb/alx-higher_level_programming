#!/usr/bin/python3

"""
This is 0-add_integer module with function add_integer(a, b), for example
>>> add_integer(1, 2)
3
"""


def add_integer(a, b=98):
    """
    adds 2 integer
    """
    if a != a:
        raise TypeError('a must be an integer')
    if b != b:
        raise TypeError('b must be an integer')
    if a is None or type(a) not in (float, int):
        raise TypeError('a must be an integer')
    if type(b) not in (float, int):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
