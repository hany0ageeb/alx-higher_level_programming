#!/usr/bin/python3

"""This Module has one function matrix_mul(m_a, m_b)
"""


def matrix_mul(m_a, m_b):
    """a function that multiplies 2 matrices
    """
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')
    if len(m_a) > 0:
        for row in m_a:
            if type(row) is not list:
                raise TypeError('m_a must be a list of lists')
    if len(m_b) > 0:
        for row in m_b:
            if type(row) is not list:
                raise TypeError('m_b must be a list of lists')
    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for item in row:
            if type(item) is not float and type(item) is not int:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for item in row:
            if type(item) is not float and type(item) is not int:
                raise TypeError("m_b should contain only integers or floats")
    m_a_row_length = len(m_a[0])
    m_b_row_length = len(m_b[0])
    for row in m_a:
        if m_a_row_length != len(row):
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if m_b_row_length != len(row):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = [[]for row in m_a]
    for row in result:
        for j in range(len(m_b[0])):
            row.append(0)
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
