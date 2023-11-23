#!/usr/bin/python3
"""
    This Module define class MagicClass
"""
import math


class MagicClass:
    """
        MagicClass reconstructed from bytecode
        Args:
            radius(float, int): Circle radius
        Attributes:
            __radius(float, int): Circle radius
        Raises:
            TypeError: if radius is not float or int
    """
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
            calculate circle areas using formula area = pi*r**2
            Returns:
                (float, int): Circle area
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
            calculate circle circumference using 2 * pi * r
            Returns:
                (float, int): circumference of circle
        """
        return 2 * math.pi * self.__radius
