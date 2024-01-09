#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for each_row in matrix:
        for integer in each_row:
            print("{:d}".format(integer), end=" ")
        print()
