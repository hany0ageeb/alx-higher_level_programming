#!/usr/bin/python3
"""
 Python script that takes in a letter and sends a POST request
 to http://0.0.0.0:5000/search_user with the letter as a parameter.
 1. The letter must be sent in the variable q
 2. If no argument is given, set q=""
 3. If the response body is properly JSON formatted and not empty,
 display the id and name like this: [<id>] <name>
 4. Otherwise:
        - Display Not a valid JSON if the JSON is invalid
        - Display No result if the JSON is empty
 5. You must use the package requests and sys
 6. You are not allowed to import packages other than requests and sys
"""
import sys
import requests
import requests.exceptions


def main():
    """Entry point"""
    q = ''
    if len(sys.argv) > 1:
        q = sys.argv[1]
    response = requests.post(
        'http://0.0.0.0:5000/search_user',
        data={'q': q})
    try:
        data = response.json()
        if data:
            print('[{}] {}'.format(data['id'], data['name']))
        else:
            print('No result')
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')


if __name__ == '__main__':
    main()
