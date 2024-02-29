#!/bin/bash
#  Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
# 1. Display only body of a 200 status code response
# 2. You have to use curl
status_code="$(curl --silent --head "$1" | awk '/^HTTP/{print $2}')"
if [ "$status_code" -eq 200 ]; then
	curl --silent "$1"
fi
