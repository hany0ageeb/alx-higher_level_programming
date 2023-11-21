#!/usr/bin/python3
class Square:
    """Square class"""
    def __init__(self, size: int = 0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self) -> int:
        """claculate area of the square as size * size"""
        return self.__size * self.__size
