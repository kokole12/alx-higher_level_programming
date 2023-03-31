#!/usr/bin/python3
""" fetching id from requests.headers"""
import sys
import requests


if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    print(res.headers['X-Request-Id'])
