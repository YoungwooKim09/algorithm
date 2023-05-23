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
 * Complete the 'connectedCell' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY matrix as parameter.
 */

function connectedCell(n, m, matrix) {
  // Write your code here
  let visited = Array.from({ length: n }, () =>
    Array.from({ length: m }, () => false)
  );

  let dx = [0, 1, 1, 1, 0, -1, -1];
  let dy = [1, 1, 0, -1, -1, -1, 0];

  let max = -10;

  function bfs(a, b) {
    let cnt = 1;
    let queue = [[a, b]];
    visited[a][b] = true;

    while (queue.length) {
      let [x, y] = queue.shift();

      for (let i = 0; i < 8; i++) {
        let nx = x + dx[i];
        let ny = y + dy[i];

        if (0 <= nx && nx < n && 0 <= ny && ny < m) {
          if (matrix[nx][ny] === 1 && !visited[nx][ny]) {
            queue.push([nx, ny]);
            cnt++;
            visited[nx][ny] = true;
          }
        }
      }
    }
    max = Math.max(max, cnt);
  }

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (!visited[i][j] && matrix[i][j]) {
        bfs(i, j);
      }
    }
  }

  return max;
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const n = parseInt(readLine().trim(), 10);

  const m = parseInt(readLine().trim(), 10);

  let matrix = Array(n);

  for (let i = 0; i < n; i++) {
    matrix[i] = readLine()
      .replace(/\s+$/g, "")
      .split(" ")
      .map((matrixTemp) => parseInt(matrixTemp, 10));
  }

  const result = connectedCell(n, m, matrix);

  ws.write(result + "\n");

  ws.end();
}
