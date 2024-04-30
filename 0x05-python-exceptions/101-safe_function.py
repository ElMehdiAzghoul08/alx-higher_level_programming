#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result_ = fct(*args)
        return result_
    except Exception as y:
        print("Exception: {}".format(y), file=sys.stderr)
        return None
