#!/usr/bin/python3
'''a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API
to display your id
You must use Basic Authentication with a personal access token
as password to access to your information (only read:user
permission is needed)
The first argument will be your username
The 2nd argument will be your password (in your case,A PAT as password)
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
Donot need to check arguments passed to the script (number or type)'''

if __name__ == '__main__':
    import requests
    import sys

    user = sys.argv[1]
    token = sys.argv[2]
    headers = {
              'Authorization': 'token {}'.format(token),
              'Accept': 'application/vnd.github.v3+json',
              }
    res = requests.get('https://api.github.com/user', headers=headers)
    print(res.json().get('id', 'None'))
