#!/usr/bin/python3

"""This Module defines Class Rectangle
"""


class Rectangle:
    """class Rectangle represents Rectangle
    Attributes:
        width (int): (Instance attribute) rectangle width >= 0
        height (int): (Instance attribute) rectangle height >= 0
        number_of_instances (int): (Class Attribute) number of intance
        print_symbol (any): (Class attribute) print symbol
    Args:
        width (int): width default 0
        height (int): height default 0
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width attribute (int)"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """height attribute (int)"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Calclate rectange area(width * height)
        Returns:
            int: width * height
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate rectangle perimeter: 2 * (width + height)
        Returns:
            0 if width or height is 0 otherwise 2 * (width + height)
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns string repre for rectangle
        """
        value = ""
        if self.__width == 0 or self.__height == 0:
            return value
        for row in range(self.__height):
            for column in range(self.__width):
                value += str(self.print_symbol)
            if row < (self.__height - 1):
                value += "\n"
        return value

    def __repr__(self):
        """returns formal represenatation for rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """print Bye rectangle... on deleting rectangle
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method that returns the biggers Rectangle based on Area
        Args:
            rect_1: first Rectangle object
            rect_2: second Rectangle object
        Raises:
            TypeError: if rect_1 or rect_2 is not instance of Rectangle
        Returns:
            (Rectangle): rect_1 if rect_1 area >= rect_2 area otherwise rect_2
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        return Rectangle(size, size)
