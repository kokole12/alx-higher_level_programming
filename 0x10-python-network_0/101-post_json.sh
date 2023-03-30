#!/bin/bash
# shell script to send a json post request to server"
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
