#!/usr/bin/node

function callMeMoby (x, TheFunction) {
  for (let counter = 1; counter <= x; counter++) {
    TheFunction();
  }
}

module.exports = { callMeMoby };
