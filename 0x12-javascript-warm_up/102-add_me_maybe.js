#!/usr/bin/node

function addMeMaybe (number, TheFunction) {
  TheFunction(parseInt(number) + 1);
}

module.exports = { addMeMaybe };
