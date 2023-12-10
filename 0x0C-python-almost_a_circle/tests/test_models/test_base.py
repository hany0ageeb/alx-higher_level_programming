#!/usr/bin/python3
"""This module contains test class for Base"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch


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
        self.assertEqual(Base.to_json_string(None), "[]")
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        self.assertEqual(Base.to_json_string([r1.to_dictionary()]),
                '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]')
