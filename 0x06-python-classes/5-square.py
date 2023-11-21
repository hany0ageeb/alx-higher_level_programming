#!/usr/bin/python3
class Square:
    def __init__(self, size: int = 0):
        self.size = size

    @property
    def size(self) -> int:
        return slef.__size

    @size.setter
    def size(self, value: int) -> None:
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self) -> int:
        """calculate area of square"""
        return self.__size * self.__size

    def my_print(self) -> None:
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
