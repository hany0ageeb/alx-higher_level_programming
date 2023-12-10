#!/usr/bin/python3
"""This module contains tests for class Square"""


import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """TestSquare class"""
    def test_square_inherits_rectangle(self):
        """test class Square inherits Rectangle"""
        self.assertTrue(issubclass(Square, Rectangle))

    def test__str__(self):
        """test return value for __str__ method"""
        s1 = Square(3, 1, 3, 1)
        self.assertEqual(str(s1), "[Square] (1) 1/3 - 3")

    def test_square_size_exist(self):
        """test squer size exist"""
        s1 = Square(3, 1, 2)
        self.assertEqual(s1.size, 3)

    def test_square_size_set_width_and_height(self):
        """test square size set inherited width and height values from rectangel"""
        s1 = Square(3, 1, 2)
        self.assertEqual(s1.width, 3)
        self.assertEqual(s1.height, 3)

    def test_square_size_raise_type_error(self):
        """test square size raise TypeError if set to str"""
        s1 = Square(3, 1, 2)
        with self.assertRaises(TypeError) as cm:
            s1.size = '1'
        self.assertEqual(str(cm.exception), 'width must be an integer')

    def test_square_size_raise_value_error(self):
        """test square size raise ValueError if set to 0"""
        s1 = Square(3, 1, 2)
        with self.assertRaises(ValueError) as cm:
            s1.size = 0
        self.assertEqual(str(cm.exception), 'width must be > 0')

    def test_update(self):
        """test suare updte method"""
        s1 = Square(3, 1, 2, 5)
        s1.update(1)
        self.assertEqual((s1.id, s1.size, s1.x, s1.y),
                         (1, 3, 1, 2))
        s1.update(2, 5)
        self.assertEqual((s1.id, s1.size, s1.x, s1.y),
                         (2, 5, 1, 2))
        s1.update(2, 5, 2, 4, 6)
        self.assertEqual((s1.id, s1.size, s1.x, s1.y),
                         (2, 5, 2, 4))
        s1.update(10, id=5)
        self.assertEqual(s1.id, 10)
        s1.update(id=500, pla=50)
        self.assertFalse(hasattr(s1, 'pla'))
        self.assertEqual(s1.id, 500)
        s1.update(size=50, x=10, y=20)
        self.assertEqual((s1.id, s1.size, s1.x, s1.y),
                         (500, 50, 10, 20))

    def test_to_dictionary(self):
        """test square to_dictionary method"""
        s1 = Square(3, 1, 2, 1)
        self.assertEqual(s1.to_dictionary(), {'id': 1, 'size': 3, 'x': 1, 'y': 2})
