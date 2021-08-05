#!/usr/bin/node
let myAargs = process.argv;
if (myAargs.length >= 4) {
  myAargs = myAargs.sort((a, b) => a - b);
  console.log(myAargs[myAargs.length - 2]);
} else {
  console.log(0);
}
