#!/usr/bin/python3
""" My github profile"""
import sys
import requests


if __name__ == "__main__":
    res = requests('https://api.github.com/user',
                   auth=(sys.argv[1], sys.argv[2]))
    print(res.json().get("id"))
