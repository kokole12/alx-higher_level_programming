#!/usr/bin/node

const lengthArr = process.argv.length;
const newArr = [];

if (process.argv.length <= 3) {
  console.log(0);
}
for (let i = 0; i < lengthArr; i++) {
  if (i >= 2) {
    newArr.push(process.argv[i]);
  }
}
const sortedList = newArr.sort();
console.log(sortedList.slice(-2, -1)[0]);
