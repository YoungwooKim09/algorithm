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
 * Complete the 'steadyGene' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts STRING gene as parameter.
 */

function steadyGene(n, gene) {
  // Write your code here
  let req = n / 4;
  let map = new Map();

  map.set("A", 0);
  map.set("C", 0);
  map.set("G", 0);
  map.set("T", 0);

  for (const str of gene) {
    map.set(str, map.get(str) + 1);
  }

  let i = 0;
  let j = 0;
  let min = 1e6;

  while (j < n && i < n) {
    if (!isSteady(map, req)) {
      map.set(gene[j], map.get(gene[j]) - 1);
      console.log(map);
      j++;
    } else {
      min = Math.min(min, j - i);
      map.set(gene[i], map.get(gene[i]) + 1);
      i++;
    }
  }

  return min;
}

function isSteady(map, N) {
  if (
    map.get("A") <= N &&
    map.get("C") <= N &&
    map.get("G") <= N &&
    map.get("T") <= N
  )
    return true;

  return false;
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const n = parseInt(readLine().trim(), 10);

  const gene = readLine();

  const result = steadyGene(n, gene);

  ws.write(result + "\n");

  ws.end();
}
