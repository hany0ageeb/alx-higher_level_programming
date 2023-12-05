#!/usr/bin/python3
"""This script adds all arguments to a Python list,
and then save them to a file"""


def load_list():
    """load arg list from add_item.json file if not exist return []"""
    load_from_json_file = (
            __import__('6-load_from_json_file').load_from_json_file)
    try:
        lst = load_from_json_file("add_item.json")
    except Exception:
        lst = []
    return lst


def add_args_to_list(lst=[]):
    """add command line args to lst"""
    import sys
    i = 1
    while i < len(sys.argv):
        lst.append(sys.argv[i])
        i += 1
    return lst


def main():
    """main entry point for script"""
    import sys
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    lst = load_list()
    add_args_to_list(lst)
    save_to_json_file(lst, "add_item.json")
    sys.exit(0)


if __name__ == '__main__':
    main()
