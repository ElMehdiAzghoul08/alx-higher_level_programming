#!/usr/bin/node

let counter_ = 0;

exports.logMe = function (item) {
  console.log(`${counter_}: ${item}`);
  counter_++;
};
