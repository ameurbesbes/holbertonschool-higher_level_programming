#!/usr/bin/node
const myVar = process.argv[2];
if (isNaN(myVar) === false) {
  for (let i = 0; i < myVar; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
