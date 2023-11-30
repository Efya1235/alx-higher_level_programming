#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in the header
of the response.
"""
import urllib.request
import sys

if len(sys.argv) == 2:
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.getheader('X-Request-Id')
            if x_request_id is not None:
                print(x_request_id)
    except Exception as e:
        pass
