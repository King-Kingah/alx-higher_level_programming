#!/usr/bin/node
let argv = process.argv;
let i = 0;
let newa = [];
if ((argv.length < 4 && parseint(argv[2]) >= 0) || !argv[2]) {
  console.log('0');
} else {
  for (i = 2; i < argv.length; 1++) {
    newa.push(parseInt(argv[i]));
  } newa = [...new Set(newa)].sort((a, b) => a - b);
  console.log(newa[newa.length - 2]);
}
