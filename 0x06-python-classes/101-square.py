#!/usr/bin/python3
"""
    This Module defines a Square class
"""


class Square:
    """
        Square class
        Attributes:
            __size(int): square size >= 0
            __position(int, int): square position as a tuple(int, int)
        Args:
            size(int): square size default value 0
            position(int, int): square position default value (0, 0)
        Raises:
            TypeError: if type(size) != int or type(position) != tuple
                        or len(position) != 2 or type of tuple value is not
                        int or their value < 0
            ValueError: if size < 0
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self) -> int:
        """
            get / set size attribute
            Args:
                value(int): int greater than or equal 0
            Raises:
                TypeError: if value is not int
                ValueError: if value < 0
            Returns:
                (int): size of square
        """
        return self.__size

    @size.setter
    def size(self, value: int) -> None:
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """
            get / ste position attribute
            Args:
                value(int, int): tuple of 2 positive int
            Raises:
                TypeError: if value not a tuple of 2 positive int
            Returns:
                (int, int): square position as tuple of int, int
        """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integer')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integer')
        if type(value[0]) is not int or type(value[0]) is not int:
            raise TypeError('position must be a tuple of 2 positive integer')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integer')
        self.__position = value

    def area(self):
        """
            calculate square area of surface
            Returns:
                int: area of square i.e size * size
        """
        return self.__size * self.__size

    def my_print(self):
        """
            print square to stdout as #, spaces
        """
        print(self)

    def __str__(self):
        """
            get str rep of square object
            Returns:
                str: a represenatation of square
        """
        value = ""
        if self.__size == 0:
            return value
        for y in range(self.__position[1]):
            value += "\n"
        for row in range(self.__size):
            for x in range(self.__position[0]):
                value += " "
            for col in range(self.__size):
                value += "#"
            if row < (self.__size - 1):
                value += "\n"
        return value
