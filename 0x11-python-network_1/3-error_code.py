#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and
displays the body of the response (decoded in utf-8).
1.  You have to manage urllib.error.HTTPError exceptions
    and print: Error code: followed by the HTTP status code
2.  You must use the packages urllib and sys
3.  You are not allowed to import other packages than urllib and sys
4.  You don’t need to check arguments passed to the script (number or type)
5.  You must use the with statement
"""
import sys
from urllib.request import urlopen
from urllib.error import HTTPError


def main():
    """Entry point"""
    try:
        with urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))


if __name__ == '__main__':
    main()
