"use strict";

const fs = require("fs");

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", function (inputStdin) {
  inputString += inputStdin;
});

process.stdin.on("end", function () {
  inputString = inputString.split("\n");

  main();
});

function readLine() {
  return inputString[currentLine++];
}

/*
 * Complete the 'minimumLoss' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts LONG_INTEGER_ARRAY price as parameter.
 */

function minimumLoss(n, price) {
  // Write your code here
  let answer = 1e16;
  let priceList = new Map();

  price.map((elem, idx) => {
    priceList.set(elem, idx);
  });

  price.sort((a, b) => b - a);

  for (let i = 0; i < n - 1; i++) {
    if (priceList.get(price[i]) < priceList.get(price[i + 1])) {
      let diff = price[i] - price[i + 1];
      answer = Math.min(answer, diff);
    }
  }

  return answer;
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const n = parseInt(readLine().trim(), 10);

  const price = readLine()
    .replace(/\s+$/g, "")
    .split(" ")
    .map((priceTemp) => parseInt(priceTemp, 10));

  const result = minimumLoss(n, price);

  ws.write(result + "\n");

  ws.end();
}
