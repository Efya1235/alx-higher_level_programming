#!/bin/bash
# Send a request to the given URL and display the response body size in bytes
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
