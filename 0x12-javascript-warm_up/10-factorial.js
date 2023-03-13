#!/usr/bin/node

const n = process.argv[2];

function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  } else {
    return (n * factorial(n - 1));
  }
}

console.log(factorial(parseInt(n)));
