#!/usr/bin/python3
"""This Module defines function is_same_class"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance of the specified class
    Args:
        obj(Any): object to check
        a_class(Any): a class to check against
    Returns:
        bool: True if the object is exactly an instance of a_class
    """
    return type(obj) is a_class
