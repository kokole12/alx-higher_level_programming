#!/usr/bin/node
const elements =  require('./100-data').list;

const new_array = elements.map(function(x, index){
    return x * index;
});

console.log(new_array);
