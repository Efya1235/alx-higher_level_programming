#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge
"""
import requests
import sys

if len(sys.argv) == 3:
    owner = sys.argv[2]
    repo = sys.argv[1]

    url = f'https://api.github.com/repos/{owner}/{repo}/commits'

    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()

        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f'{sha}: {author_name}')
    else:
        print("API request failed. Check repository and owner names.")
else:
    print("Usage: ./100-github_commits.py <repository> <owner>")
