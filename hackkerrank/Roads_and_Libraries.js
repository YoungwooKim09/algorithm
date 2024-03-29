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
 * Complete the 'roadsAndLibraries' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER c_lib
 *  3. INTEGER c_road
 *  4. 2D_INTEGER_ARRAY cities
 */
function dfs(group, node, adj) {
  if (!group.has(node)) {
    group.add(node);

    for (const adjCity of adj[node]) {
      dfs(group, adjCity, adj);
    }
  }

  return group;
}

function roadsAndLibraries(n, c_lib, c_road, cities) {
  // Write your code here
  if (c_lib <= c_road) return n * c_lib;

  let cost = 0;
  let adj = Array.from({ length: n + 1 }, () => []);
  let visited = new Set();

  cities.forEach((elem) => {
    adj[elem[0]].push(elem[1]);
    adj[elem[1]].push(elem[0]);
  });

  for (let i = 1; i <= n; i++) {
    if (!visited.has(i)) {
      let cityGroup = dfs(new Set(), i, adj);

      cost += c_lib + c_road * (cityGroup.size - 1);

      cityGroup.forEach((city) => {
        visited.add(city);
      });
    }
  }

  return cost;
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const q = parseInt(readLine().trim(), 10);

  for (let qItr = 0; qItr < q; qItr++) {
    const firstMultipleInput = readLine().replace(/\s+$/g, "").split(" ");

    const n = parseInt(firstMultipleInput[0], 10);

    const m = parseInt(firstMultipleInput[1], 10);

    const c_lib = parseInt(firstMultipleInput[2], 10);

    const c_road = parseInt(firstMultipleInput[3], 10);

    let cities = Array(m);

    for (let i = 0; i < m; i++) {
      cities[i] = readLine()
        .replace(/\s+$/g, "")
        .split(" ")
        .map((citiesTemp) => parseInt(citiesTemp, 10));
    }

    const result = roadsAndLibraries(n, c_lib, c_road, cities);

    ws.write(result + "\n");
  }

  ws.end();
}
