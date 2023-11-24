#!/usr/bin/python

"""
Module 5-text_indentation which contains func text_indentation(text)
"""



def text_indentation(text):
    """
    a function that prints a text with 2 new lines after
    each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    for ch in text:
        print(ch, end='')
        if ch in ('.', '?', ':'):
            print()
            print()
