#!/usr/bin/python3
""" returns the value of X-Request-Id from headers"""
import sys
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        headers = response.getheaders()
        # print(headers)
        # for header in headers:
        #     print(header)
        dict_body = dict(headers)
        print(dict_body.get("X-Request-Id"))
