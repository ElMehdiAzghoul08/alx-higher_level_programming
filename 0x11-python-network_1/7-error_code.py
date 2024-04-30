#!/usr/bin/python3
"""takes in a URL, sends a request to the URL
and displays the body of the rp_"""
import requests
import sys

if __name__ == "__main__":
    url_ = sys.argv[1]

    rp_ = requests.get(url_)

    if rp_.status_code >= 400:
        print("Error code:", rp_.status_code)
    else:
        print(rp_.text)
