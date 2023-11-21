#!/usr/bin/python3
"""
    module 2-square which define a simple Square class
"""


class Square:
    """
    class Square - represents a simple Square with size
    Attributes:
        size(int): square size should be >= 0
    """
    def __init__(self, size: int = 0):
        """
        __init__ function - initialize Square object
        Args:
            size(int): the size of the quare
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
