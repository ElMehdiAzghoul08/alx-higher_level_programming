#!/usr/bin/node

const argument = process.argv.slice(2);
const r = argument.map(argument => parseInt(argument));

console.log(biggest_(r));

function biggest_ (r) {
  if (r.length <= 1) {
    return 0;
  } else {
    return Math.max(...r);
  }
}
