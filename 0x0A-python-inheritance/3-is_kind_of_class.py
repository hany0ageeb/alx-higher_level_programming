#!/usr/bin/python3
"""This module defines a function: is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class
    Args:
        obj(Any): object to test
        a_class(Any): a class to test against
    Returns:
        bool: True if obj is an instance of a_class ,
        or a class the inherit from a_class
    """
    return isinstance(obj, a_class)
