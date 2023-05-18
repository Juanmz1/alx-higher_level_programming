#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is not str  or roman_string is None:
        return 0
    romans = { 'I': 1, 'V': 5,' X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
            }
    result = 0
    keys = list(roman.keys())
    for i in roman_string[::-1]:
        if keys.index(roman_string[1]) < keys.index(roman_string[i + 1]:
                result -= romans[roman_string[i]]
        else:
        result += romans[roman_string[i]]
    result += roman(roman_string[-1])
    return result
