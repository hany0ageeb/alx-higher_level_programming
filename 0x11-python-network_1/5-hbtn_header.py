#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
1. You must use the packages requests and sys
2. You are not allow to import other packages than requests and sys
3. The value of this variable is different for each request
4. You don’t need to check script arguments (number and type)
"""
import sys
import requests


def main():
    """Entry point"""
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))


if __name__ == '__main__':
    main()
