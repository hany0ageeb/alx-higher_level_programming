#!/usr/bin/python3
"""This module defines a single function: append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, "r") as f:
        lines = f.readlines()
    for index, line in enumerate(lines):
        if search_string in line:
            lines.insert(index + 1, new_string)
    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
