#!/usr/student/python3
"""This module defines a single class: Student"""


class Student:
    """class Student
    Attributes:
        first_name(str): (instance attribute) student first name
        last_name(str): (instance attribute) student last name
        age(int): (instance attribute) student age
    Args:
        first_name(str): first name
        last_name(str): last name
        age(int): age
    """
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return dict(self.__dict__)
        dictionary = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                dictionary[key] = value
        return dictionary
