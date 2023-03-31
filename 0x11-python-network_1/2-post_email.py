#!/usr/bin/python3
""" Sends  post request """
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    email = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')
    url = sys.argv[1]
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.rea()
        body_str = body.decode('utf-8')
        print(body_str)
