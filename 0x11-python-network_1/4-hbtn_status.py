#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
1. You must use the package requests
2. You are not allow to import packages other than requests
3. The body of the response must be display like
   the following example (tabulation before -)
guillaume@ubuntu:~/0x11$ ./4-hbtn_status.py | cat -e
Body response:$
    - type: <class 'str'>$
    - content: OK$
guillaume@ubuntu:~/0x11$
"""
import requests


def main():
    """Entry point"""
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(response.text)))
    print('\t- content: {}'.format(response.text))


if __name__ == '__main__':
    main()
