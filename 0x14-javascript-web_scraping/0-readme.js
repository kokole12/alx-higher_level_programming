#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];
fs.readFile(__dirname + "/" + filename,
(err, data) => {
    if (err) {
        console.log(err);
        return;
    }
    console.log(data)
} );
