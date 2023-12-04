#!/usr/bin/python3
"""This module defines a single function: add_attribute"""


def add_attribute(obj: any, attr_name: str, attr_value: any):
    """
    adds a new attribute to an object if it’s possible
    Args:
        obj(any): object to add attribute to
        attr_name(str): attribute name
        attr_value(any): attribute value
    Raises:
        TypeError: if obj cannot has new attributes
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
