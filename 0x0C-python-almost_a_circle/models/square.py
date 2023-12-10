#!/usr/bin/python3
"""This module defines a single class: Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square  that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self) -> int:
        """size getter or setter
        Args:
            value(int): new square size value
        Raises:
            TypeError: if value is not integer
            ValueError: if value <= 0
        Returns:
            (int): current Square size
        """
        return self.width

    @size.setter
    def size(self, value: int) -> None:
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """public method that assigns attributes"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key in ('id', 'size', 'x', 'y'):
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
        }

    def to_list(self):
        """returns the list repr of a Square"""
        return [self.id, self.size, self.x, self.y]
