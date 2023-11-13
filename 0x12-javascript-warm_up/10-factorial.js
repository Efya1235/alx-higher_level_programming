#!/usr/bin/node

function computeFactorial (n) {
  if (isNaN(n)) {
    return 1;
  }

  if (n <= 1) {
    return 1;
  }

  return n * computeFactorial(n - 1);
}

const input = Number(process.argv[2]);
const factorial = computeFactorial(input);

console.log(`${factorial}`);
