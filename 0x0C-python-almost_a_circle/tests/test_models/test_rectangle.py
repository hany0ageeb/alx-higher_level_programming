#!/usr/bin/python3
"""This module contains tests for class Rectangle"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """class TestRectangle"""
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
        """test width type error message should
        be 'width must be an integer'"""
        with self.assertRaises(TypeError) as cm:
            r = Rectangle("1", 2)
        self.assertEqual(str(cm.exception), 'width must be an integer')

    def test_width_should_raise_value_error_if_passed_value_zero(self):
        """test if width raises ValueError if given a value of zero"""
        with self.assertRaises(ValueError) as cm:
            r = Rectangle(0, 2)

    def test_width_value_error_message(self):
        """test width should raise value error
        with message 'width must be > 0'"""
        with self.assertRaises(ValueError) as cm:
            r = Rectangle(0, 2)
        self.assertEqual(str(cm.exception), 'width must be > 0')

    def test_width_should_raise_type_error_if_passed_float(self):
        """set setting width to float should raise TypeError"""
        r = Rectangle(2, 2)
        with self.assertRaises(TypeError) as cm:
            r.width = 1.0
        self.assertEqual(str(cm.exception), 'width must be an integer')

    def test_height_exist(self):
        """test height property exist"""
        r = Rectangle(2, 2)
        self.assertTrue(r.height)

    def test_height_retrieve_correct_value(self):
        """test height property should return correct value"""
        r = Rectangle(2, 2)
        self.assertEqual(r.height, 2)

    def test_height_should_raise_type_error(self):
        """setting Rectangle height to non int should raise type error"""
        with self.assertRaises(TypeError) as cm:
            r = Rectangle(1, '1')
        self.assertEqual(str(cm.exception), 'height must be an integer')

    def test_height_should_raise_value_error_on_zero(self):
        """test setting height to zero should raise valueerror"""
        with self.assertRaises(ValueError) as cm:
            r = Rectangle(1, 0)
        self.assertEqual(str(cm.exception), 'height must be > 0')

    def test_height_should_raise_type_error_if_given_float(self):
        """test setting height to float 1.0 should raise TypeError"""
        with self.assertRaises(TypeError) as cm:
            r = Rectangle(1, 1.0)
        self.assertEqual(str(cm.exception), 'height must be an integer')

    def test_x_property_exist(self):
        """test x property exist"""
        r = Rectangle(1, 1, 1, 1)
        self.assertTrue(r.x)

    def test_x_property_getter_retrive_correct_value(self):
        """test x retrive the assigned value"""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.x, 3)

    def test_x_setter_raise_type_error_if_passed_str(self):
        """test setting x to '1' should raise TypeError"""
        with self.assertRaises(TypeError) as cm:
            r = Rectangle(1, 2, '1', 3)
        self.assertEqual(str(cm.exception), 'x must be an integer')

    def test_x_setter_raise_type_error_if_passed_float(self):
        """test setting x to float('1.0') should raise TypeError"""
        with self.assertRaises(TypeError) as cm:
            r = Rectangle(1, 2, float('1'), 3)

    def test_setting_x_to_value_less_than_zero_should_raise_value_error(self):
        """test setting x to -1 should raise value error"""
        with self.assertRaises(ValueError) as cm:
            r = Rectangle(1, 2, -1, 1)
        self.assertEqual(str(cm.exception), 'x must be >= 0')

    def test_y_exist(self):
        """test y property setter/getter working properly"""
        r = Rectangle(1, 1, 1, 2)
        self.assertEqual(r.y, 2)

    def test_y_property_should_raise_type_error_if_passed_str(self):
        """test y should raise typeError if set to str '1'"""
        with self.assertRaises(TypeError) as cm:
            r = Rectangle(1, 2, 3, '1')
        self.assertEqual(str(cm.exception), 'y must be an integer')

    def test_y_property_should_raise_type_error_if_pased_float(self):
        """test y should raise TypeError if set to float('1')"""
        with self.assertRaises(TypeError) as cm:
            r = Rectangle(1, 2, 3, float('1'))

    def test_setting_y_to_negative_one_should_raise_value_error(self):
        """test setting y to -1 should raise value error"""
        with self.assertRaises(ValueError) as cm:
            r = Rectangle(1, 2, 3, -1)
        self.assertEqual(str(cm.exception), 'y must be >= 0')

    def test_area(self):
        """test area method"""
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)
        r.width = 7
        r.height = 8
        self.assertEqual(r.area(), 56)
        r.width = 2
        r.height = 10
        self.assertEqual(r.area(), 20)

    def test_to_str(self):
        """test return value of """
        r1 = Rectangle(4, 6)
        self.assertEqual(r1.to_str(), "####\n####\n####\n####\n####\n####")
        r1 = Rectangle(2, 2)
        self.assertEqual(r1.to_str(), "##\n##")
        r1 = Rectangle(2, 3, 2, 2)
        self.assertEqual(r1.to_str(), "\n\n  ##\n  ##\n  ##")
        r1 = Rectangle(3, 2, 1, 0)
        self.assertEqual(r1.to_str(), " ###\n ###")

    def test__str__(self):
        """test Rectangle __str__ method return correct value"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        r1 = Rectangle(5, 5, 1, 0, 1)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/0 - 5/5")

    def test_update_args(self):
        """test rectangle update method"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual((r1.id, r1.width, r1.height, r1.x, r1.y),
                         (89, 10, 10, 10, 10))
        r1.update(88, 5)
        self.assertEqual((r1.id, r1.width, r1.height, r1.x, r1.y),
                         (88, 5, 10, 10, 10))
        r1.update(87, 5, 6)
        self.assertEqual((r1.id, r1.width, r1.height, r1.x, r1.y),
                         (87, 5, 6, 10, 10))
        r1.update(85, 2, 7, 0)
        self.assertEqual((r1.id, r1.width, r1.height, r1.x, r1.y),
                         (85, 2, 7, 0, 10))
        r1.update(80, 1, 2, 3, 4)
        self.assertEqual((r1.id, r1.width, r1.height, r1.x, r1.y),
                         (80, 1, 2, 3, 4))
        with self.assertRaises(TypeError) as cm:
            r1.update(8, '1')
        self.assertEqual(str(cm.exception), 'width must be an integer')
        with self.assertRaises(ValueError) as cm:
            r1.update(8, 1, 0)
        self.assertEqual(str(cm.exception), 'height must be > 0')
        with self.assertRaises(TypeError) as cm:
            r1.update(8, 1, 2, '1')
        self.assertEqual(str(cm.exception), 'x must be an integer')
        with self.assertRaises(ValueError) as cm:
            r1.update(8, 1, 2, 0, -1)
        self.assertEqual(str(cm.exception), 'y must be >= 0')

    def test_update_kwargs(self):
        """test rectangle update method"""
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(5, id=1)
        self.assertEqual((r1.id, r1.width, r1.height, r1.x, r1.y),
                         (5, 10, 10, 10, 10))
        r1.update(id=2)
        self.assertEqual((r1.id, r1.width, r1.height, r1.x, r1.y),
                         (2, 10, 10, 10, 10))
        r1.update(pla=1, id=50)
        self.assertEqual(r1.id, 50)
        self.assertFalse(hasattr(r1, 'pla'))
        self.assertEqual(r1.id, 50)
        r1 = Rectangle(10, 10, 10, 10, 1)
        r1.update(width=20, height=30, id=50)
        self.assertEqual((r1.id, r1.width, r1.height, r1.x, r1.y),
                         (50, 20, 30, 10, 10))

    def test_to_dictionary(self):
        """test rectangle to dictionary method"""
        r1 = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(r1.to_dictionary(),
                         {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9})
