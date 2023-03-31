#!/usr/bin/python3
""" handles the httperror"""
import sys
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.request.HTTPError as e:
        print("Error code: {}".format(e.code))
