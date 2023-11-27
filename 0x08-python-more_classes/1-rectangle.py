#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This Module 1-Rectangle defines class: Rectangle
"""


class Rectangle:
    """
    class Rectangle that defines a rectangle by
    Args:
        width (int): width of rectangle
        height (int): height of rectangle
    Attributes:
        width (int): width of rectangle
        height (int): height of rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        rectnagle width property (int)
        Args:
            value (int): new width value
        Raises:
            TypeError: if value is not int
            ValueError: if value < 0
        Returns:
            int: rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        rectangle height property
        Args:
            value (int): new height value
        Raises:
            TypeError: if value not int
            ValueError: if value < 0
        Returns:
            int: rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
