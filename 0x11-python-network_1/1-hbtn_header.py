#!/usr/bin/python3
"""
A Python scrippt that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found
in the header of the resposne
Requirements:
1. use packages urllib and sys
2. do not import any pakcages other than urllib and sys
3. The value of this variable is different for each request
4. do bot check arguments
5. must use with statement
"""
from urllib.request import urlopen
import sys


def main():
    """Entry Point"""
    with urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))


if __name__ == '__main__':
    main()