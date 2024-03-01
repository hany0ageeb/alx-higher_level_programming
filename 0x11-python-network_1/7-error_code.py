#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL
and displays the body of the response.

1.  If the HTTP status code is greater than or equal to 400,
    print: Error code: followed by the value of the HTTP status code
2.  You must use the packages requests and sys
3.  You are not allowed to import packages other than requests and sys
4.  You don’t need to check arguments passed to the script (number or type)
"""
import sys
import requests


def main():
    """Entry point"""
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.text)


if __name__ == '__main__':
    main()
