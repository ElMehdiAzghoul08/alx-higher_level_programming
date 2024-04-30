#!/usr/bin/python3
"""script that takes 2 arguments in order to solve this challenge"""
import requests
import sys

if __name__ == "__main__":
    repo_nm = sys.argv[1]
    owner_nm = sys.argv[2]

    url_ = f"https://api.github.com/repos/{owner_nm}/{repo_nm}/commits"
    rp_ = requests.get(url_)
    commits = rp_.json()

    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
