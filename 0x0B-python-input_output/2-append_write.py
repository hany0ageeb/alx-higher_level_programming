#!/usr/bin/python3
"""This module defines a single function: append_write"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""
    with open(filename, "a", encoding="utf-8") as f:
        n_written = f.write(text)
    return n_written
