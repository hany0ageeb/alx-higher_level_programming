#!/usr/bin/python3
"""This module defines a single function: to_json_string"""


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string)"""
    import json
    return json.dumps(my_obj)
