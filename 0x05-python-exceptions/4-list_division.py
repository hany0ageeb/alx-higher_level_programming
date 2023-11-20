#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = [0.0 for i in range(list_length)]
    for i in range(list_length):
        try:
            result[i] = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
    return result
