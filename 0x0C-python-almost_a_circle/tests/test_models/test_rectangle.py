#!/usr/bin/python3
"""This module contains tests for class Rectangle"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_width_exist(self):
        """test if rectangle class has width property"""
        r = Rectangle(1, 2)
        self.assertTrue(r.width)

    def test_width_retrive_correct_value(self):
        """test if width property getter return the right value"""
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)

    def test_width_should_raise_type_error_if_passsed_non_int(self):
        """test if width raise TypeError if passed str"""
        with self.assertRaises(TypeError) as cm:
            r = Rectangle("1", 2)

    def test_width_type_error_message(self):
        """test width type error message should be 'width must be an integer'"""
        with self.assertRaises(TypeError) as cm:
            r = Rectangle("1", 2)
        self.assertEqual(str(cm.exception), 'width must be an integer')

    def test_width_should_raise_value_error_if_passed_value_zero(self):
        """test if width raises ValueError if given a value of zero"""
        with self.assertRaises(ValueError) as cm:
            r = Rectangle(0, 2)
    def test_width_value_error_message(self):
        """test width should raise value error with message 'width must be > 0'"""
        with self.assertRaises(ValueError) as cm:
            r= Rectangle(0, 2)
        self.assertEqual(str(cm.exception), 'width must be > 0')

    def test_width_should_raise_type_error_if_passed_float(self):
        """set setting width to float should raise TypeError"""
        r = Rectangle(2, 2)
        with self.assertRaises(TypeError) as cm:
            r.width = 1.0
        self.assertEqual(str(cm.exception), 'width must be an integer')

