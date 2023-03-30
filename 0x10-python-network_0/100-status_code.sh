#!/bin/bash
# shell script to return the status code of a reques
curl -s -o /dev/null -w "%{http_code}" "$1"
