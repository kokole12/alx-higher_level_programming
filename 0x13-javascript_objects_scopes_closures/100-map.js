#!/usr/bin/node

const elements = require('./100-data').list;

const newArray = elements.map((x, index) => {
  return x * index;
});

console.log(elements);
console.log(newArray);
