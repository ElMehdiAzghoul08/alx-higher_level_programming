#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    digit = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = [digit[a] for a in roman_string] + [0]
    r = 0

    for n in range(len(num) - 1):
        if num[n] >= num[n+1]:
            r += num[n]
        else:
            r -= num[n]

            return r
