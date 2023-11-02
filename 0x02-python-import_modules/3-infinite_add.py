#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    result = 0
    length = len(sys.argv)
    while i < length:
        result += int(sys.argv[i])
        i += 1
    print("{}".format(result))
