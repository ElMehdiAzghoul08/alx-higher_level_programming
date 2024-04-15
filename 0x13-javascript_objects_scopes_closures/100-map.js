#!/usr/bin/node

const { list } = require('./100-data');

const new_ = list.map((val_, idx) => val_ * idx);

console.log(list);
console.log(new_);
