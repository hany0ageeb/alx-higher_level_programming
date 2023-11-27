#!/usr/bin/python3

"""
1-Rectangle Module: Defines Rectangle class
"""


class Rectangle:
    """
    Rectangle class represents a rectangle with width and height
    Attributes:
        width (int): rectangle width
        height (int): rectangle height
    """
    def __init__(self, width=0, height=0):
        """
        Args:
            width (int): width default 0
            height (int): height default 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        rectangle width property (setter/getter)
        Args:
            value (int): new width value >= 0
        Raises:
            TypeError: if value is not int
            ValueError: if value < 0
        Returns:
            int : width
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
        """Rectangle height property (setter/getter)
        Args:
            value (int): new height value >= 0
        Raises:
            TypeError: if value is not int
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

    def area(self):
        """computes rectangle area as width multiplied by height
        Returns:
            int: rectangle area which is width * height
        """
        return self.__width * self.__height

    def perimeter(self):
        """Computes rectangle perimeter as 2 * (width + height)
        Returns:
            int: if either width or height is 0 return 0 otherwise
            return 2 * (width + height)
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
