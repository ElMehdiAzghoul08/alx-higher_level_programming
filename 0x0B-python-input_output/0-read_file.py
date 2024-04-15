#!/usr/bin/python3

"""Define read file function"""


def read_file(filename=""):
    """read file function"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
