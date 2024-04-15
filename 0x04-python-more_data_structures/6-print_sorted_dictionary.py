#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key_ in sorted(a_dictionary.keys()):
        print("{}: {}".format(key_, a_dictionary[key_]))
