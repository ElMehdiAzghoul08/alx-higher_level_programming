#!/usr/bin/python3
def magic_calculation(a, b):
    result_ = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result_ += (a ** b) / i
        except Exception:
            result_ = b + a
            break
    return result_
