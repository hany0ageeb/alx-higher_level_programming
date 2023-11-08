#!/usr/bin/python3
def weight_average(my_list=[]):
    left = 0
    right = 0
    for a_tuple in my_list:
        left += (a_tuple[0] * a_tuple[1])
        right += a_tuple[1]
    if right == 0:
        return 0
    return left / right
