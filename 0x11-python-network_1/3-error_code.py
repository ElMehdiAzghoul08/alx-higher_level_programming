#!/usr/bin/python3
"""takes in a URL, sends a request to the URL
and displays the body of the rp_ (decoded in utf-8)"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url_ = sys.argv[1]

    try:
        with urllib.request.urlopen(url_) as rp_:
            ctxt = rp_.read().decode('utf-8')
            print(ctxt)
    except urllib.error.HTTPError as y:
        print("Error code:", y.code)