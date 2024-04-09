#!/usr/bin/node

const argument = process.argv;

if (argument[2] !== undefined && argument[3] === undefined) {
  console.log(argument[2] + ' ' + 'is' + ' ' + ' ' + argument[3]);
} else if (argument[2] === undefined && argument[2] !== undefined) {
  console.log(argument[2] + ' ' + 'is' + ' ' + argument[3]);
} else {
  console.log(argument[2] + ' ' + 'is' + ' ' + argument[3]);
}
