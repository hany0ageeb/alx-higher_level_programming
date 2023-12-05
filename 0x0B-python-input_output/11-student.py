#!/usr/bin/python3
"""This module defines a single class: Student
"""


class Student:
    """class Student
    Attributes:
        first_name(str): (Instance attribute) student first name
        last_name(str): (Instance attribute) student last name
        age(int): (Instance attribute) student age
    Args:
        first_name(str): first name
        last_name(str): last name
        age(int): age
    """
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age: int = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance
        args:
            attrs(list of str): attributes to retrive
        """
        if attrs is None:
            return dict(self.__dict__)
        tmp = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                tmp[key] = value
        return tmp

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance"""
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
