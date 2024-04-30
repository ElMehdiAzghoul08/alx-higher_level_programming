#!/usr/bin/node

const { list } = require("./100-dta_");

const new_ = list.map((val_, idx) => val_ * idx);

console.log(list);
console.log(new_);
