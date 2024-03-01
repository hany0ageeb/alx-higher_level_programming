#!/usr/bin/python3
"""
The Holberton School staff evaluates candidates applying
for a back-end position with multiple technical challenges,
like this one: Please list 10 commits (from the most
recent to oldest) of the repository “rails” by the user “rails”
You must use the GitHub API,
here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
Write a Python script that takes 2 arguments in order to solve this challenge.
1. The first argument will be the repository name
2. The second argument will be the owner name
3. You must use the packages requests and sys
4. You are not allowed to import packages other than requests and sys
5. You don’t need to check arguments passed to the script (number or type)
"""
import sys
import requests


def main():
    """Entry Point"""
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
            sys.argv[2],
            sys.argv[1])
    headers = {
        'Accept': 'application/vnd.github+json',
        # 'Authorization': 'Bearer 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',
        'X-GitHub-Api-Version': '2022-11-28',
    }
    data = {
        'per_page': 10,
        'page': 1
    }
    response = requests.get(
        url,
        headers=headers,
        data=data
    )
    if response.status_code == requests.codes.ok:
        commits = response.json()
        for commit in commits:
            print('{}: {}'.format(
                commit['sha'],
                commit['commit']['author']['name']))


if __name__ == '__main__':
    main()
