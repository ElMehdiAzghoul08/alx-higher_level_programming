#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == "__main__":
    url_ = 'https://alx-intranet.hbtn.io/status'

    rp_ = requests.get(url_)

    print("Body rp_:")
    print("\t- type:", type(rp_.text))
    print("\t- content:", rp_.text)
