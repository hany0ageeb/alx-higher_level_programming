#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response.
curl --silent --request POST ----data-urlencode "catch_me=True" 0.0.0.0:5000/catch_me
