#!/usr/bin/python3
class Square:
    def __init__(self, size: int = 0, position: (int, int) = (0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, value: int) -> None:
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('ize must be >= 0')
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value: (int, int)) -> None:
        if type(value) != tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2 or type(value[0]) != int or type(value[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self) -> int:
        return self.__size * self.__size

    def my_print(self) -> None:
        for y in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for x in range(self.__position[0]):
                print(' ', end='')
            for j in range(self.__size):
                print("#", end='')
            print()
        if self.__size == 0:
            print()
