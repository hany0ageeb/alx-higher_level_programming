#!/usr/bin/python3
def row_sqrt(row=[]):
    return list(map(lambda num: num * num, row))
def square_matrix_simple(matrix=[]):
    return list(map(row_sqrt, matrix))
