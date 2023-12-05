#!/usr/bin/python3
"""This module defines a single class: Student"""


class Student:
    """class Student
    Attributes:
        first_name(str): (Instance attribute) student first name
        las_name(str): (Instance attribute) student last name
        age(int): (Instance attribute) student age
    """
    def __init__(self, first_name, last_name, age):
        """Initialize new Student object
        Args:
            first_name(str): student first name
            last_name(str): studnet last name
            age(int): student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
