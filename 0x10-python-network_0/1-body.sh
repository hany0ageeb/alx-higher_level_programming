#!/bin/bash
#  Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
# 1. Display only body of a 200 status code response
# 2. You have to use curl
status_code="$(curl -s --head "$1" | awk '/^HTTP/{print $2}')"
if [[ "$status_code" == "200" ]]; then
	curl -s "$1"
fi
