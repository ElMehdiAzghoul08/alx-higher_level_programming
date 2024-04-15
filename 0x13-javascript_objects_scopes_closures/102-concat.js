#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const contentA_ = fs.existsSync(fileA) ? fs.readFileSync(fileA, 'utf8') : '';
const contentB_ = fs.existsSync(fileB) ? fs.readFileSync(fileB, 'utf8') : '';

const concatContent_ = contentA_ + '\n' + contentB_ + '\n';

fs.writeFileSync(fileC, concatContent_);
