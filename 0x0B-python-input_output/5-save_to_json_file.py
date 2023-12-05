#!/usr/bin/python3
"""This module contains a single function: save_to_json_file"""


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation"""
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
