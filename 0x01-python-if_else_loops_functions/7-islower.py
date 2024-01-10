#!/usr/bin/python3
def islower(c):
    if ord("a") <= ord(c) <= ord("z"):
        print(f"{c} is lower")
        return True
    else:
        return False
