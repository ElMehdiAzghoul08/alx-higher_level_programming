#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for each_row in matrix:
        for i, integer in enumerate(each_row):
            print("{:d}".format(integer), end="")
            if i < len(each_row) - 1:
                print(" ", end="")
        print()
