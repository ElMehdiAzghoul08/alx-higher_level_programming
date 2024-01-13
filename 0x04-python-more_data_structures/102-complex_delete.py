#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    _key_del = [key_ for key_, val_ in a_dictionary.items() if val_ == value]

    for key_ in _key_del:
        a_dictionary.pop(key_)

        return a_dictionary
