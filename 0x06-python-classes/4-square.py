#!/usr/bin/python3
"""
   This Module defines a simple Square class
"""


class Square:
    """
        A simple Square class
        Attributes:
            size(int): instance attribute represent size
        Raises:
            TypeError: if size is not an integer
            ValueError: if size < 0
    """
    def __init__(self, size: int = 0):
        self.size = size

    @property
    def size(self) -> int:
        """
            square size getter
            Returns:
                int: the size of square
        """
        return self.__size

    @size.setter
    def size(self, value: int) -> None:
        """
            square size setter
            Args:
                value(int): the new value of size attr
            Raises:
                TypeError: if value is not an integer
                ValueError: if value < 0
        """
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self) -> int:
        """
            calculate the area of the square
            Returns:
                int: square area (i.e. size * size)
        """
        return self.__size * self.__size
