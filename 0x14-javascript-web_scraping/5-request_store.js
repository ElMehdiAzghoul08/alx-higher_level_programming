#!/usr/bin/node
const fs_ = require('fs');
const req_ = require('request');

req_(process.argv[2]).pipe(fs_.createWriteStream(process.argv[3]));
