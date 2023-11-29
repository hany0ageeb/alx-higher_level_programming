#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    TestMaxInteger - tests max_integer function
    """
    def test_max_integer(self):
        """
        tests max_integer edge cases
        """
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([1, 3, 2]), 3)
        self.assertIsNone(max_integer([]))
        with self.assertRaises(TypeError):
            result = max_integer([1, 2, 3, 'a'])
        self.assertIsNone(max_integer())
        self.assertEqual(max_integer("123"), '3')
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')
        with self.assertRaises(TypeError):
            result = max_integer(1.5)
        self.assertEqual(max_integer([5, 4, 3, 2]), 5)
        self.assertEqual(max_integer([1, 2, 5]), 5)
        self.assertEqual(max_integer([6.5, 1.0, 2.5]), 6.5)
