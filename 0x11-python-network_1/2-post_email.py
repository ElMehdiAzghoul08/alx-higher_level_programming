#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url_ = sys.argv[1]
    email = sys.argv[2]

    dta_ = urllib.parse.urlencode({'email': email}).encode()

    rst_ = urllib.request.Request(url_, dta_=dta_, method='POST')

    with urllib.request.urlopen(rst_) as rp_:
        ctxt = rp_.read().decode('utf-8')

    print(ctxt)
