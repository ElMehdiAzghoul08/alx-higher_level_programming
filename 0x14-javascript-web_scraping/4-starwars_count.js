#!/usr/bin/node
const req_ = require('request');

const urlApI_ = process.argv[2];
const idChar_ = '18';

req_(urlApI_, (erro_, res_, body) => {
  if (erro_) {
    console.error(erro_);
    return;
  }
  if (res_.statusCode === 200) {
    const wedgeChAr_ = JSON.parse(body).results.filter(film_ => film_.characters.includes(`https://swapi-api.alx-tools.com/api/people/${idChar_}/`));
    console.log(wedgeChAr_.length);
  }
});
