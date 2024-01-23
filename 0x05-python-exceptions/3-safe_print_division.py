#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result_ = a / b
    except ZeroDivisionError:
        result_ = None
    finally:
        print("Inside result: {}".format(result_))
        return result_
