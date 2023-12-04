#!/usr/bin/python3
"""This module defines Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class represensts Rectangle
    Attributes:
        width(int): (instance attribute) rectangle width
        width(int): (instance attribute) rectangle height
    """
    def __init__(self, width, height):
        """
            Args:
                width(int): must be int > 0
                height(int): must be int > 0
            Raises:
                TypeError: if width or height is not int
                ValueError: if widh or height is <= 0
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """computes rectangle area (width * height)
        Returns:
            int: rectangle area i.e. width*height
        """
        return self.__width * self.__height

    def __str__(self):
        """create a string representatuoin for rectangel
        Returns:
            str: [Rectangle] width/height
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
