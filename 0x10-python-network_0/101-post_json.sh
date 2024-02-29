#!/bin/bash
# Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl --silent --request POST --header "Content-Type: application/json" --data "$(cat "$2")" "$1"
