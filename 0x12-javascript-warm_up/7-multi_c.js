#!/usr/bin/node

const argument = process.argv[2];
const phrase = 'C is fun';
let counter = 1;

const x = parseInt(argument);
if (isNaN(x)) {
  console.log('Missing number of occurrences');
}

while (counter <= x) {
  console.log(phrase);
  counter++;
}
