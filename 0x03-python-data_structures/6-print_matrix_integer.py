#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for i in range(0, len(matrix)):
        row = matrix[i]
        if row is None:
            continue
        for j in range(0, len(row)):
            print("{:d}".format(row[j]), end=' ')
        print()
