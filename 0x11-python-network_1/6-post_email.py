#!/usr/bin/python3
"""
Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
1. The email must be sent in the variable email.
2. You must use the packages requests and sys.
3. You are not allowed to import packages other than requests and sys.
4. You don’t need to error check arguments passed to the script.
"""
import sys
import requests


def main():
    """Entry point"""
    response = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(response.text)


if __name__ == '__main__':
    main()
