#!/usr/bin/node

const a = parseInt(process.argv[2]);

console.log(factorial_(a));

function factorial_ (a) {
  if (isNaN(a) || a === 1 || a === undefined) {
    return 1;
  }
  return a * factorial_(a - 1);
}
