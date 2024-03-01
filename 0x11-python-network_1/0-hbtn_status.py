#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
from urllib.request import urlopen


def main():
    """
    Entry point
    """
    with urlopen('https://alx-intranet.hbtn.io/status') as response:
        response_body = response.read()
        print('Body response:')
        print('    - type: {}'.format(type(response_body)))
        print('    - content: {}'.format(response_body))
        print('    - utf8 content: {}'.format(response_body.decode('utf8')))


if __name__ == '__main__':
    main()
