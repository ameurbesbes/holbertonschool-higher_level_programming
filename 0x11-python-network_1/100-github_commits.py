#!/usr/bin/python3
"""
List most recent to oldest commits (10) of the repository "rails" by the user
"rails"
"""
import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    repo = owner_name + "/" + repo_name
    url = "https://api.github.com/repos/" + repo + "/commits"
    r = requests.get(url)
    for i in r.json()[:10]:
        sha = i['sha']
        author = i['commit']['author']['name']
        print('{}: {}'.format(sha, author))
