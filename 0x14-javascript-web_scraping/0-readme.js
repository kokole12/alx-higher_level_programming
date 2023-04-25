#!/usr/bin/node

const fs = require('fs');
const path = require('path');
const filename = process.argv[2];
fs.readFile(path.join(__dirname, '/', filename), 'utf-8',
  (err, data) => {
    if (err) {
      console.log(err);
      return;
    }
    console.log(data);
  });
