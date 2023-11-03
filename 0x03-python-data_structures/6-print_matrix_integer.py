#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        row = matrix[i]
        for j in range(0, len(row)):
            print(row[j], end=' ')
        print()
