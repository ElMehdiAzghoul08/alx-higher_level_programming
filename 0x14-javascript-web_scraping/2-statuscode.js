#!/usr/bin/node
const req_ = require('request');

const url_ = process.argv[2];

req_(url_, (erro_, res_, body) => {
  if (erro_) {
    console.error('Error:', erro_);
    return;
  }
  console.log(`code: ${res_.statusCode}`);
});
