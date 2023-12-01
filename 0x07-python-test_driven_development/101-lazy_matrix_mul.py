#!/usr/bin/python3

"""This Module has only one function
lazy_matrix_mul(m_a, m_b) that multiply 2 matrix
using numpy
"""


def lazy_matrix_mul(m_a, m_b):
    """
    multiply 2 matrices using numpy package
    """
    import numpy as np

    return np.dot(m_a, m_b)
