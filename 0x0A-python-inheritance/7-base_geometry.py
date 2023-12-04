#!/usr/bin/python3
"""This module define class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry
    Instance Methods:
        area
        integer_validator
    """
    def area(self):
        """raises an Exception with message: areas() is not implemented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates value
        Args:
            name(str): name
            value(int): value to validate
        Raises:
            TypeError: if value is not int
            ValueError: if value is <= 0
        Returns:
            None: if validation passed
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
        return True
