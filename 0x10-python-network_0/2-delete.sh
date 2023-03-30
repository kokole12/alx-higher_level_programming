#!/bin/bash
# shell script that sends a delete request to server at port 5000
curl -sX DELETE "$1"
