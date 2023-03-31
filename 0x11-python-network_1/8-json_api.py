#!/usr/bin/python3
""" sends a requesr with a query paramater"""
import sys
import requests
import json


if __name__ == "__main__":
    param = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": param}

    res = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        response = res.json()
        if response == {}:
            print('No result')
        else:
            print('[{}] {}'.format(response.get('id'), response.get("name")))
    except ValueError:
        print('Not a valid Json')
