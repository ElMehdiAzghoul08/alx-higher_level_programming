#!/usr/bin/python3
""" takes in a URL and an email address,
sends a POST request to the passed URL
with the email as a parameter"""
import requests
import sys

if __name__ == "__main__":
    url_ = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}

    rp_ = requests.post(url_, data=data)

    print(rp_.text)
