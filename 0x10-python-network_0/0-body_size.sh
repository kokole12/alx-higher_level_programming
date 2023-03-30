#!/bin/bash
# shell script to send request to url and display size in bytes of the response
curl -s "$1" | wc -c
