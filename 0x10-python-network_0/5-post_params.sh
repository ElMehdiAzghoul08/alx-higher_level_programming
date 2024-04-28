#!/bin/bash
# script that takes in a URL, sends a POST request to passed URL,displays body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
