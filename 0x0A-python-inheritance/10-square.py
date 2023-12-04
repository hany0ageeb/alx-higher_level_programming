#!/usr/bin/python3
"""This module defines a single class: Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangel"""
    def __init__(self, size):
        """initialize a square object
        Args:
            size(int): square size must be int > 0
        """
        super().__init__(size, size)

    def area(self):
        """calculate square area"""
        return super().area()
