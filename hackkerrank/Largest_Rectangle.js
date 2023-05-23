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
 * Complete the 'largestRectangle' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts INTEGER_ARRAY h as parameter.
 */

function largestRectangle(n, h) {
  // Write your code here
  let maxArea = 0;

  let index = 0;
  let stack = [];

  while (index < n) {
    if (stack.length == 0 || h[stack[stack.length - 1]] <= h[index]) {
      stack.push(index++);
    } else {
      let top = stack.pop();
      let area =
        h[top] *
        (stack.length > 0 ? index - stack[stack.length - 1] - 1 : index);
      maxArea = Math.max(maxArea, area);
    }
  }

  while (stack.length > 0) {
    let top = stack.pop();
    let area =
      h[top] * (stack.length > 0 ? index - stack[stack.length - 1] - 1 : index);

    maxArea = Math.max(maxArea, area);
  }

  return maxArea;
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const n = parseInt(readLine().trim(), 10);

  const h = readLine()
    .replace(/\s+$/g, "")
    .split(" ")
    .map((hTemp) => parseInt(hTemp, 10));

  const result = largestRectangle(n, h);

  ws.write(result + "\n");

  ws.end();
}
