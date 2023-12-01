#!/usr/bin/python3

"""
Module 5-text_indentation which contains func text_indentation(text)
"""


def text_indentation(text):
    line_begin = True
    """
    a function that prints a text with 2 new lines after
    each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    for ch in text:
        if line_begin and ch != ' ':
            print(ch, end='')
            line_begin = False
        elif not line_begin:
            print(ch, end='')
        if ch in ('.', '?', ':'):
            print()
            print()
            line_begin = True
