#!/usr/bin/python3
"""
    1-square module defines a simple Square class
    Square class has a private instance property __size
"""


class Square:
    """
        Square class represents Square with size

        Attributes:
            size(int): the size of quare should be >= 0
    """
    def __init__(self, size):
        """
            this function initizliize Square object with the given size
            size should be positive integer >= 0
            but we do not check for that yet
            Args:
                size (int): initial size of the Square
        """
        self.__size = size
