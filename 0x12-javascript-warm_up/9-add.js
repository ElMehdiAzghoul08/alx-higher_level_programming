#!/usr/bin/node

const argument = process.argv;
const a = argument[2];
const b = argument[3];

console.log(add(a, b));

function add (a, b) {
  if (a === undefined || b === undefined) {
    return NaN;
  }
  const Result = parseInt(a) + parseInt(b);
  return Result;
}
