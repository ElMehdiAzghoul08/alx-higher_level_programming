#!/usr/bin/python3

""" takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id"""

import urllib.request
import sys

if __name__ == "__main__":
    url_ = sys.argv[1]

    rst_ = urllib.request.Request(url_)

    with urllib.request.urlopen(rst_) as rp_:
        id_rst = rp_.headers.get('X-Request-Id')

    print(id_rst)