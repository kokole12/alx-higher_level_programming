#!/usr/bin/python3
""" My github profile"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests('https://api.github.com/user', auth=auth)
    print(res.json().get("id"))
