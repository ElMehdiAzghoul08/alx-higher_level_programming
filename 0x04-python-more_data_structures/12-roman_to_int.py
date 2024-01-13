#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    roman_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    val = 0
    for n in reversed(roman_string):
        val = roman_n[n]
        reasult += val if result < val * 5 else -val
    return result
