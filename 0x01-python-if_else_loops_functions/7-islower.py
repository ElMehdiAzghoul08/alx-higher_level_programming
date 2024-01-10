#!/usr/bin/python3
def islower(c):
    if ord("a") <= ord(c) <= ord("z"):
        print(f"{c} is lower")
        return True
    else:
        print(f"{c} is upper")
        return False
