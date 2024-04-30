#!/usr/bin/python3
"""takes your GitHub credentials (username and password)"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url_ = 'https://api.github.com/user'

    rp_ = requests.get(url_, auth=(username, password))

    if rp_.status_code == 200:
        info_ = rp_.json()
        print(info_['id'])
    else:
        print(None)
