#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_digit = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    number = 0
    for c in roman_string[::-1]:
        value = roman_digit.get(c, 0)
        if value >= number:
            result += value
        else:
            result -= value
        number = value
    return result
