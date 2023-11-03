#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    value_1 = tuple_a[0] if len(tuple_a) > 0 else 0
    value_2 = tuple_b[0] if len(tuple_b) > 0 else 0
    value_3 = tuple_a[1] if len(tuple_a) > 1 else 0
    value_4 = tuple_b[1] if len(tuple_b) > 1 else 0
    return value_1 + value_2, value_3 + value_4
