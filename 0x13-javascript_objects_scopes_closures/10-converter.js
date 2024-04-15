#!/usr/bin/node

exports.converter = function (base){
    return function (result_){
        return result_.toString(base);
    };
};