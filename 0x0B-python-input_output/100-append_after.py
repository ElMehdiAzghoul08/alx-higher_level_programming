#!/usr/bin/python3

"""Defines append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """append_after function"""
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
