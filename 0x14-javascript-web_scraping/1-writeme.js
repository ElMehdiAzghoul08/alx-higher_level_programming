#!/usr/bin/node
const fs_ = require('fs');

const filePath_ = process.argv[2];
const ctnt_ = process.argv[3];

fs_.writeFile(filePath_, ctnt_, 'utf-8', (erro_) => {
  if (erro_) {
    console.erro_(erro_);
  }
});
