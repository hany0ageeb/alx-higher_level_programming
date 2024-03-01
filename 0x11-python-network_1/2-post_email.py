#!/usr/bin/python3
"""
A python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the resposne(decode in utf-8)
1. The email must be sent in the email variable.
2. you must use the packages urllib and sys
3. you must use with statment
"""
import sys
from urllib.request import urlopen
from urllib.parse import urlencode


def main():
    """Entry Point"""
    with urlopen(
            sys.argv[1],
            data=urlencode({
                'email': sys.argv[2]
                }).encode('ascii')) as response:
        print(response.read().decode('utf8'))


if __name__ == '__main__':
    main()
