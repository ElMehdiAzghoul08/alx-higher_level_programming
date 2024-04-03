#!/usr/bin/python3

"""Defines load_from_json_file function"""
import json


def load_from_json_file(filename):
    """load_from_json_file function"""
    with open(filename) as f:
        return json.load(f)
