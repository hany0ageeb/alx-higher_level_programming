#!/usr/bin/python3
"""
    This module represents a Square class
"""


class Square:
    """
        class Square
        Args:
            size(int): size of square >= 0
        Attributes:
            __size(int): size of square >= 0
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """
            get/set size of square
            Args:
                value(int): value of size >= 0
            Raises:
                TypeError: if value is not int
                ValueError: if value < 0
            Returns:
                int: size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be a number')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
            calculate area of a square
            Returns:
                int: square area as size * size
        """
        return self.__size * self.__size

    def __lt__(self, other):
        """
            overloading < operator
            Args:
                other(Square): other square
            Returns:
                bool: True if area of self is less than other otherwise False
        """
        if other is None:
            return False
        return self.area() < other.area()

    def __le__(self, other):
        """
            overloading <= operator
            Args:
                other(square): other square
            Returns:
                bool: True if self.area() <= other.area() otherwise False
        """
        if other is None:
            return False
        return self.area() <= other.area()

    def __eq__(self, other):
        """
            overloading == operator
            Args:
                other(Square): other square
            Returns:
                bool: True if self.area() == other.area() othersies False
        """
        if other is None:
            return False
        return self.area() == other.area()

    def __ne__(self, other):
        """
            overloading != operator
            Args:
                other(Square): other square
            Returns:
                bool: True if self.area() != other.area() otherwise False
        """
        if other is None:
            return False
        return self.area() != other.area()

    def __gt__(self, other):
        """
            overloading > operator
            Args:
                other(Square): other square
            Returns:
                bool: True if self.area() > other.area() otherwise False
        """
        if other is None:
            return False
        return self.area() > other.area()

    def __ge__(self, other):
        """
            overloading >= operator
            Args:
                other(Square): other square
            Returns:
                bool: True if self.area() >= other.area()
        """
        if other is None:
            return False
        return self.area() >= other.area()
