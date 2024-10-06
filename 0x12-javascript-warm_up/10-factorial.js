#!/usr/bin/node

let num = 1;

if (parseInt(process.argv[2])) {
  num = parseInt(process.argv[2]);
}

function factorial (a) {
  if (a <= 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

console.log(factorial(num));
