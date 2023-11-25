#!/usr/bin/python3

"""This Module has only one function
lazy_matrix_mul(m_a, m_b) that multiply 2 matrix
using numpy
"""


class InvalidTypeError(Exception):
    """
    InvalidTypeException class replaces TypeError
    """
    def __init__(self, message):
        super().__init__(message)


class EmptyListError(Exception):
    """
    EmptyListError class if list is [] or [[]]
    """
    def __init__(self, message):
        super().__init__(message)


class NotRectangleListError(Exception):
    """
    NotRectangleListError raised when list ia not rectangle
    """
    def __init__(self, message):
        super().__init__(message)


def lazy_matrix_mul(m_a, m_b):
    """
    multiply 2 matrices using numpy package
    """
    import numpy as np

    m_a_row_len = -1
    m_b_row_len = -1
    m_a_has_diff_row_len = False
    m_b_has_diff_row_len = False
    if type(m_a) is not list:
        raise InvalidTypeError('m_a should be a list')
    if type(m_b) is not list:
        raise InvalidTypeError('m_b should be a list')
    for row in m_a:
        if type(row) is not list:
            raise InvalidTypeError('m_a is not a list of lists(matrix)')
        else:
            if m_a_row_len == -1:
                m_a_row_len = len(row)
            elif m_a_row_len != len(row):
                m_a_has_diff_row_len = True
    for row in m_b:
        if type(row) is not list:
            raise InvalidTypeError('m_b is not a list of lists(matrix)')
        else:
            if m_b_row_len == -1:
                m_b_row_len = len(row)
            elif m_b_row_len != len(row):
                m_b_has_diff_row_len = True
    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise EmptyListError('m_a cannot be an empty list ([] or [[]])')
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise EmptyListError('m_b cannot be an empty list ([] or [[]])')
    for row in m_a:
        for item in row:
            if type(item) not in (int, float):
                raise InvalidTypeError('m_a should be a list of lists \
containing only floats or ints')
    for row in m_b:
        for item in row:
            if type(item) not in (int, float):
                raise InvalidTypeError('m_b should be a list of lists \
containing only floats or ints')
    if m_a_has_diff_row_len:
        raise NotRectangleListError('m_a must be a rectangle matrix')
    if m_b_has_diff_row_len:
        raise NotRectangleListError('m_b must be a rectangle matrix')
    return np.dot(m_a, m_b)
