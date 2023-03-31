#!/usr/bin/python3
""" Creating a post request with requests"""
import sys
import requests


if __name__ == "__main__":
    res = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(res.text)
