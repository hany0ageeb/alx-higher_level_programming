#!/usr/bin/python3
"""This module defines a single function: append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file,
    after each line containing a specific string
    """
    if search_string == "" or new_string == "":
        return
    with open(filename, "r") as fin, open("tmp", "w") as fout:
        for line in fin:
            fout.write(line)
            if search_string in line:
                fout.write(new_string)
    with open(filename, "w") as fout, open("tmp", "r") as fin:
        for line in fin:
            fout.write(line)
