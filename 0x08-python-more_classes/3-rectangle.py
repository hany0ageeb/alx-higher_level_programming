#!/usr/bin/python3
"""This Module defines a single class Rectangle
"""


class Rectangle:
    """Rectangle class represent a rectangle with width and height
    Attributes:
        width (int): rectangle width >= 0
        height (int): rectangle height >= 0
    Args:
        width (int): rectangle width >= 0
        height (int): rectangle height >= 0
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width property of rectangle
        Args:
            value (int): new width value of rectangle
        Raises:
            TypeError: if value is not int
            ValueError: if value < 0
        Returns:
            int: rectangle width value
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
        """height property of rectangle
        Args:
            value (int): new height value
        Raises:
            TypeError: if value is not int
            ValueError: if value < 0
        Returns:
            int: height of rectangle
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
        """Calculates area of rectangle (i.e. width * height)
        Returns:
            int: width * height
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates perimeter of rectangle
        Returns:
            int: 0 if width or height is 0 otherwise 2 * (width + height)
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """implements __str__ method
        Returns:
            str: nice represenation of object rectangle
        """
        value = ""
        if self.__width == 0 or self.__height == 0:
            return value
        for row in range(self.__height):
            for column in range(self.__width):
                value += "#"
            if row < (self.__height - 1):
                value += "\n"
        return value
