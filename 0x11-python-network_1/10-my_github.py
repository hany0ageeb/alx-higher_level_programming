#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
1.  You must use Basic Authentication with a personal access token as password
    to access to your information (only read:user permission is needed)
2.  The first argument will be your username
3.  The second argument will be your password
    (in your case, a personal access token as password)
4.  You must use the package requests and sys
5.  You are not allowed to import packages other than requests and sys
6.  You don’t need to check arguments passed to the script (number or type)
"""
import sys
import requests


def main():
    """Entry Point"""
    url = 'https://api.github.com/users/' + sys.argv[1]
    response = requests.get(
        url,
        headers={
            'Accept': 'application/vnd.github+json',
            'Authorization': 'Bearer ' + sys.argv[2],
            'X-GitHub-Api-Version': '2022-11-28'})
    data = response.json()
    print(data.get('id', None))


if __name__ == '__main__':
    main()
