#!/bin/bash
#script that takes in a URL and displays HTTP methods the server will accept

curl -sI -X OPTIONS "$1" | grep -i "Allow" | cut -d " " -f 2-
