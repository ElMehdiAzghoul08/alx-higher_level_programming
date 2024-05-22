#!/usr/bin/node
const fs_ = require('fs');

const filePath_ = process.argv[2];
fs_.readFile(filePath_, 'utf-8', (erro_, ctnt_) => {
  if (erro_) {
    console.error(erro_);
    return;
  }
  console.log(ctnt_);
});
