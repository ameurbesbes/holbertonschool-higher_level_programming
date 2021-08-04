#!/usr/bin/node
const myVar = process.argv[2];
if (isNaN(myVar)) {
  console.log('Missing size');
} else {
  const size = parseInt(myVar);

  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
