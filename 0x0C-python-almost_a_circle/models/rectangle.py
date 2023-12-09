#!/usr/bin/python3
"""This module defines a single class: Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle: represent a rectangle
    Attributes:
        width(int): (Instance Attribute) rectangle width
        height(int): (Instance Attribute) rectangle height
        x(int): (Instance Attribute) rectangle x position
        y(int): (Instance Attribute) rectangle y position
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get or set Rectangle width
        Args:
            value(int): new width
        Raises:
            TypeError: if value is not int
            ValueError: if value <= 0
        Returns:
            (int): current rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self) -> int:
        """Get or set Rectangle height
        Args:
            value(int): new height
        Raises:
            TypeError: if value is not int
            ValueError: if value <= 0
        Returns:
            (int): current rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self) -> int:
        """Get or Set Rectangle x position
        Args:
            value(int): new Rectangle x position
        Raises:
            TypeError: if value is not integer
            ValueError: if value < 0
        Returns:
            (int): current Rectangle x value
        """
        return self.__x

    @x.setter
    def x(self, value: int) -> None:
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self) -> int:
        """Get or Set Rectangle y value
        Args:
            value(int): new Rectangle y position
        Raises:
            TypeError: if value is not integer
            ValueError: if value < 0
        Returns:
            (int): the current Rectangle y position
        """
        return self.__y

    @y.setter
    def y(self, value: int) -> None:
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """calculate rectangle area: width * height
        Returns:
            (int): rectangle area as width * height
        """
        return self.width * self.height

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def to_str(self):
        """return str to display rectangle on stdout"""
        reper = ""
        reper += self.y * "\n"
        for row in range(self.height):
            reper += self.x * " " + self.width * "#"
            if row < (self.height - 1):
                reper += "\n"
        return reper

    def display(self):
        """print in stdout the Rectangle instance with the character #
        """
        print(self.to_str())

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle"""
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
        }

    def to_list(self):
        """returns the list representation of Rectangle"""
        return [
                self.id,
                self.width,
                self.height,
                self.x,
                self.y]

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key in ('id', 'width', 'height', 'x', 'y'):
                    setattr(self, key, value)
