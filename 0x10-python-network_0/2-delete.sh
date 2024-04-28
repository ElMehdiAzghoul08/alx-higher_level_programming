#!/bin/bash
#sends a DELETE request to the URL passed as the first argument and displays body

curl -sX DELETE "$1"
