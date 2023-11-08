#!/usr/bin/python3
def uniq_add(my_list=[]):
    added_numbers = []
    result = 0
    for num in my_list:
        if num not in added_numbers:
            result += num
            added_numbers.append(num)
    return result
