#!/bin/bash
# Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl --silent --head "$1" | grep -i Allow | cut -d ':' -f 2 | sed -e 's/^[ \t]*//'
