#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials
(username and password) and uses the
GitHub API to display your id
"""

import requests
import sys

if len(sys.argv) == 3:
    username = sys.argv[1]
    personal_access_token = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, personal_access_token))

    if response.status_code == 200:
        user_info = response.json()
        print(user_info['id'])
    else:
        print("None")
