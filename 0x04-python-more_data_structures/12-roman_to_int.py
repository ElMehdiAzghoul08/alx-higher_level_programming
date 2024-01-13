#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }

    total_ = 0
    prev_value_ = 0

    for numeral_ in reversed(roman_string):
        value_ = roman_numerals[numeral_]

        if value_ < prev_value_:
            total_ -= value_
        else:
            total_ += value_

        prev_value_ = value_

    return total_
