#!/usr/bin/python3
"""
    This Module defines a Square class with size and position
"""


class Square:
    """
        Square class
        Attributes:
            size(int): square size >= 0
            position((int, int)): square positon(x, y)
        Args:
            size(int): square size default 0 should be >= 0
            position((int, int)): square position default (0, 0)
        Raises:
            TypeError: if type of size is not intgere
            ValueError: if size < 0
            TypeError: if position is not a tuple or if  length not 2
                        or contains non positive int values
    """
    def __init__(self, size: int = 0, position: (int, int) = (0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self) -> int:
        """
            get Square size
            Args:
                value(int): new size value >= 0
            Raises:
                TypeError: if value is not int
                ValueError: if value < 0
            Returns:
                int: ths size of square
        """
        return self.__size

    @size.setter
    def size(self, value: int) -> None:
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('ize must be >= 0')
        self.__size = value

    @property
    def position(self):
        """
            get/set square position
            Args:
                value(int, int): new posiiton value
            Raises:
                TypeError: if position is not tuple or a tuple that
                does not contain exactly to positive(>=0) integers
            Returns:
                (int, int): the square position as tuple(int, int)
        """
        return self.__position

    @position.setter
    def position(self, value: (int, int)) -> None:
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self) -> int:
        """
            calculates the square area
            Returns:
                (int): size * size
        """
        return self.__size * self.__size

    def my_print(self) -> None:
        """
           print Square to stdout using # and spaces
        """
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
