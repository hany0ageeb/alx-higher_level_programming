#!/usr/bin/python3
"""This module defines a single function: from_json_string"""


def from_json_string(my_str):
    """eturns an object (Python data structure) represented by a JSON string"""
    import json
    return json.loads(my_str)
