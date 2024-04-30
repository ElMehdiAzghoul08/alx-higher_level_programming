#!/usr/bin/node

const argument = process.argv;

if (Number.isInteger(parseInt(argument[2]))) {
  console.log('My number: ' + parseInt(argument[2]));
} else {
  console.log('Not a number');
}
