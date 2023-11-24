#!/usr/bin/python3

"""
Module 2-matrix_divided
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix
    """
    valid_types = (int, float)
    if type(div) not in valid_types:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    row_length = -1
    result = []
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) \
of integers/floats')
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError('matrix must be a matrix (list of lists) \
of integers/floats')
        else:
            result.append([])
            if row_length == -1:
                row_length = len(matrix[i])
            else:
                if row_length != len(matrix[i]):
                    raise TypeError('Each row of the matrix must \
have the same size')
            for j in range(row_length):
                if type(matrix[i][j]) not in valid_types:
                    raise TypeError('matrix must be a matrix (list of lists) \
of integers/floats')
                else:
                    result[i].append(round(matrix[i][j] / div, 2))
    return result
