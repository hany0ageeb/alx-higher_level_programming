#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    length = len(sys.argv)
    if length == 1:
        print("{} arguments.".format(length - 1))
    elif length == 2:
        print("{} argument:".format(length - 1))
    else:
        print("{} arguments:".format(length - 1))
    i = 1
    while i < length:
        print("{}: {}".format(i, sys.argv[i]))
        i += 1
