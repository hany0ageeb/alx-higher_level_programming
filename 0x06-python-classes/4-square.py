#!/usr/bin/python3
class Square:
    def __init__(self, size: int = 0):
        self.size = size

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, value: int) -> None:
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise TypeError('size must be >= 0')
        self.__size = value

    def area(self) -> int:
        return self.__size * self.__size
