#!/usr/bin/piython3
# -*- coding: utf-8 -*-
"""This module contains test class for Base"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """class TestBase"""
    def test_Base_init(self):
        """test __init__ method of Base"""
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(50)
        self.assertEqual(b3.id, 50)

    def test_to_json_string(self):
        """test to_json static method"""
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None),
                         "[]")
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        expected_rslt = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(Base.to_json_string([r1.to_dictionary()]),
                         expected_rslt)

    def test_save_to_file(self):
        """test save_to_file method"""
        pass

    def test_from_json_string(self):
        """test from_json_string method"""
        pass

    def test_create(self):
        """test create method"""
        pass

    def test_load_from_file(self):
        """test load_from_file"""
        pass

    def test_create(self):
        """test create class method"""
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), str(r2))
        self.assertTrue(r1 != r2)
        s1 = Square.create(id=5, size=10, x=1, y=2)
        self.assertEqual((s1.id, s1.size, s1.x, s1.y),
                         (5, 10, 1, 2))

    def test_update(self):
        """test update instance method"""
        b = Base()
        b.update(14)
        self.assertEqual(b.id, 14)
        b.update(15, id=10)
        self.assertEqual(b.id, 15)
        b.update(id=10)
        self.assertEqual(b.id, 10)
        b.update(id=5, pla=1)
        self.assertFalse(hasattr(b, 'pla'))
