#!/usr/bin/python3
def print_last_digit(number):
    for last_digit in number:
        if number >= 0:
            last_digit = number % 10
            print(f"{last_digit}", end="")
        else:
            last_digit = number % -10
            print(f"{last_digit}", end="")
