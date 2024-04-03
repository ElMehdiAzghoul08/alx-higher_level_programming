#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key_ in list(a_dictionary.keys()):
        if a_dictionary[key_] == value:
            del a_dictionary[key_]
    return a_dictionary
