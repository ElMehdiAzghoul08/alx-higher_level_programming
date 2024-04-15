#!/usr/bin/node

const { dict } = require('./101-data');

const DictOfOct_ = {};

for (const [id_, occ_] of Object.entries(dict)) {
  if (!DictOfOct_[occ_]) {
    DictOfOct_[occ_] = [];
  }
  DictOfOct_[occ_].push(id_);
}

console.log(DictOfOct_);
