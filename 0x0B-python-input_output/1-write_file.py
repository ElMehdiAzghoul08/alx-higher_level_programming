#!/usr/bin/python3

"""Defines write file function."""


def write_file(filename="", text=""):
    """write_file function"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
