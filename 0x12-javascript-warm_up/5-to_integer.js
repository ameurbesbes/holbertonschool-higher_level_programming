#!/usr/bin/node

const myVar = process.argv[2];
if (isNaN(myVar) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(myVar));
}
