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
        print("""Body Response:
    - type: {}
    - content: {}
    - utf8 content: {}""".format(
            type(response_body),
            response_body,
            response_body.decode('utf8')))


if __name__ == '__main__':
    main()
