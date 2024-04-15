#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list(map(lambda b: list(map(lambda a: a ** 2, b)), matrix))
    return new_matrix
