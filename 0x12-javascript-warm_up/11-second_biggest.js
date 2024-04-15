#!/usr/bin/node

const argument = process.argv.slice(2);
const r = argument.map(argument => parseInt(argument));

console.log(biggest_(r));

function biggest_ (r) {
  if (r === 0 || r === 1) {
    return 0;
  }
  return Math.max(...r);
}
