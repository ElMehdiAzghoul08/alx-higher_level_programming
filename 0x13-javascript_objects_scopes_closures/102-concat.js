#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const contentA_ = fs.readFileSync(fileA, 'utf8');
const contentB_ = fs.readFileSync(fileB, 'utf8');

const concatContent_ = contentA_.trim() + '\n' + contentB_.trim() + '\n';

fs.writeFileSync(fileC, concatContent_);
