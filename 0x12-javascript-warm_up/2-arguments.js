#!/usr/bin/node

const argument = process.argv;

if (argument.length === 3) {
  console.log('Argument found');
} else if (argument.length > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
