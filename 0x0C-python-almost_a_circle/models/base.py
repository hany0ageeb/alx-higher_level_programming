#!/usr/bin/python3
"""This module defines a single class: Base
"""

import json
import csv


class Base:
    """Class Bas: is the "base" for all other classes in the project
    Attributes:
        __nb_objects(int): (Class Attribute) ids counter
        id(int): (Instance Attribute) id
    Args:
        id(int): id if none increment __nb_objects and assign it to id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None or type(id) is not int:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def update(self, *args, **kwargs):
        """update method of Base"""
        if args:
            self.id = args[0]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries
        Args:
            list_dictionaries(list): a list of dictionaries
        Returns:
            (str): If list_dictionaries is None or empty,
            return the string: "[]" otherwise return
            the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries, sort_keys=False)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method that writes the JSON string representation
        of list_objs to a file"""
        list_dict = []
        if list_objs is not None:
            for obj in list_objs:
                if issubclass(cls, Base):
                    list_dict.append(obj.to_dictionary())
        with open(f'{cls.__name__}.json', 'w') as f:
            f.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """that returns the list of the JSON string
        representation json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        from models.square import Square
        from models.rectangle import Rectangle
        if cls is Rectangle:
            dummy = cls(1, 1)
        elif cls is Square:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        instances = []
        try:
            with open(f'{cls.__name__}.json', 'r') as f:
                list_dict = Base.from_json_string(f.read())
            for inst_dict in list_dict:
                instances.append(cls.create(**inst_dict))
            return instances
        except FileNotFoundError:
            return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes and deserializes in CSV"""
        with open(f'{cls.__name__}.csv', 'w', newline='') as f:
            csvwriter = csv.writer(f)
            for obj in list_objs:
                csvwriter.writerow(obj.to_list())

    @classmethod
    def load_from_file_csv(cls):
        """returns a list of instances"""
        instances = []
        try:
            with open(f"{cls.__name__}.csv", "r", newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    dummy = cls(1, 1)
                    data = list(
                            map(
                                lambda x: int(x)
                                if type(x) is str and x.isnumeric()
                                else None,
                                row))
                    dummy.update(*data)
                    instances.append(dummy)
            return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        pass
