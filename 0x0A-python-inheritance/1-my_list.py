#!/usr/bin/python3
"""This Module defines My_list class"""


class MyList(list):
    """My_list class inherits list classs"""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
