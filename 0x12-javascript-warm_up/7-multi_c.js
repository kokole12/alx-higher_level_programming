#!/usr/bin/node
const argc0 = process.argv[2];
if (!parseInt(argc0)) {
  console.log('Missing number of occurences');
}
for (let i = 0; i < argc0; i++) {
  console.log('C is fun');
}
