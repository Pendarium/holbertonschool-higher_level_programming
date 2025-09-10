#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    values = [romans[char] for char in roman_string]

    total = 0
    for i in range(len(values)):
        if i + 1 < len(values) and values[i] < values[i + 1]:
            total -= values[i]
        else:
            total += values[i]
    return total
