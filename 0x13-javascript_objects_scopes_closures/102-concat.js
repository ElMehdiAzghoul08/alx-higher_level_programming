#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const contentA_ = fs.existsSync(fileA) ? fs.readFileSync(fileA, 'utf8').trim() : '';
const contentB_ = fs.existsSync(fileA) ? fs.readFileSync(fileB, 'utf8').trim() : '';

const concatContent_ = contentA_ + (contentA_ && contentB_ ? '\n' : '') + contentB_;

fs.writeFileSync(fileC, concatContent_);
