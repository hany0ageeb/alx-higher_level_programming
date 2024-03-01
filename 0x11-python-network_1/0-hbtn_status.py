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
        print('\t- type: {}'.format(type(response_body)))
        print('\t- content: {}'.format(response_body))
        print('\t- utf8 content: {}'.format(response_body.decode('utf8')))


if __name__ == '__main__':
    main()
