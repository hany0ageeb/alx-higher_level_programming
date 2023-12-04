#!/usr/bin/python3
"""This module defines a single class: MyInt that inherits from int"""


class MyInt(int):
    """class MyInt inherits int"""
    def __eq__(self, otherValue):
        """reverse of =="""
        return super().__ne__(otherValue)

    def __ne__(self, otherValue):
        """reverse of != of int"""
        return super().__eq__(otherValue)
