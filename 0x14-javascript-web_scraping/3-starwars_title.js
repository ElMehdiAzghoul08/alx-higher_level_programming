#!/usr/bin/node
const req_ = require('request');

const idMov_ = process.argv[2];
const url_ = `https://swapi-api.alx-tools.com/api/film_s/${idMov_}`;

req_(url_, (erro_, res_, body) => {
  if (erro_) {
    console.error(erro_);
    return;
  }
  const mov_ = JSON.parse(body);
  console.log(mov_.title);
});
