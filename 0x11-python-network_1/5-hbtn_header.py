#!/usr/bin/python3
"""takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id"""
import requests
import sys

if __name__ == "__main__":
    url_ = sys.argv[1]

    rp_ = requests.get(url_)

    id_rst = rp_.headers.get('X-Request-Id')

    print(id_rst)
