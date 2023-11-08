#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return None
    total_value = 0
    current_value = 0
    next_value = 0
    roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }
    index = 0
    length = len(roman_string)
    while index < length:
        current_value = roman_numerals[roman_string[index]]
        if index < (length - 1):
            next_value = roman_numerals[roman_string[index + 1]]
        else:
            next_value = 0
        if current_value < next_value:
            total_value += (next_value - current_value)
            index += 1
        else:
            total_value += current_value
        index += 1
    return total_value
