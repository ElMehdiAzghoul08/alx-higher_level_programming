#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    for integer in reversed(my_list):
        print("{:d}".format(integer))
