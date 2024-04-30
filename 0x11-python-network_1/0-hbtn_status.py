#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":

    import urllib.request

    url_ = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url_) as rp_:
        ctxt = rp_.read()
        print("Body response:")
        print("\t- type:", type(ctxt))
        print("\t- content:", ctxt)
        print("\t- utf8 content:", ctxt.decode('utf-8'))
