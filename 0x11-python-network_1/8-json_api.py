#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    dta_ = {'q': q}

    rp_ = requests.post('http://0.0.0.0:5000/search_user', data=dta_)

    try:
        json_rp_ = rp_.json()
        if json_rp_:
            print("[{}] {}".format(json_rp_['id'], json_rp_['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
