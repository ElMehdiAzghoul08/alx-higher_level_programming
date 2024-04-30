#!/usr/bin/node

const argument = process.argv[2];

const column = argument;
const row = argument;

if (argument == null) {
  console.log('Missing size');
}

for (let i = 1; i <= row; i++) {
  let rowInLine = '';
  for (let a = 1; a <= column; a++) {
    rowInLine = rowInLine + 'X';
  }
  console.log(rowInLine);
}
