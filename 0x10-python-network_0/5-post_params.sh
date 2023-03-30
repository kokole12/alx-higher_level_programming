#!/bin/bash
# shell script to send an post request and some conrent"
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
