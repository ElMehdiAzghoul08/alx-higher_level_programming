#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result_ = fct(*args)
        return result_
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
