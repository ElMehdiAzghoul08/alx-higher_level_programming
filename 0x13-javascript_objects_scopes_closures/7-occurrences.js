#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counter_ = 0;
  for (let a = 0; a < list.length; a++) {
    if (list[a] === searchElement) {
      counter_++;
    }
  }
  return counter_++;
};
