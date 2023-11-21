#!/usr/bin/python3
"""
    module 3-square:
        define a simple Square class
"""


class Square:
    """
        class Square:
            a simple Square with size
        Args:
            size(int): the size of square >= 0 defaults to 0
        Attributes:
            size(int): square size
        Raises:
            TypeError: if size is not an integer
            ValueError: if size < 0
    """
    def __init__(self, size: int = 0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self) -> int:
        """
            claculate area of the square as size * size
            Returns:
                int: the area of square = size * size
        """
        return self.__size * self.__size
