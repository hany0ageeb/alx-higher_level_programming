#!/usr/bin/python3
"""
    This Module defines a simple Square class
"""


class Square:
    """
        This class represents a Square with size
        Attributes:
            size(int): Square size >= 0
        Args:
            size(int): square size >= 0 default value 0
        Raises:
            TypeError: if type(size) != int
            ValueError: if size < 0
    """
    def __init__(self, size: int = 0):
        self.size = size

    @property
    def size(self) -> int:
        """
            get square size
            Returns:
                int: self.__size
        """
        return slef.__size

    @size.setter
    def size(self, value: int) -> None:
        """
            set square size to given value
            Args:
                value(int): new size value
            Raises:
                TypeError: if type(value) != int
                ValueError: if value < 0
        """
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self) -> int:
        """
            calculate area of square
            Returns:
                int: area of square (size * size)
        """
        return self.__size * self.__size

    def my_print(self) -> None:
        """
            print square to stdout wit #
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
