#!/bin/bash
# shell script to retrun the allpw section of the header file
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
