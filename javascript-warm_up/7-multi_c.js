#!/usr/bin/node

const x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else if (x > 0) {
  const output = [];
  for (let i = 0; i < x; i++) {
    output.push('C is fun');
  }
  console.log(output.join('\n'));
}
