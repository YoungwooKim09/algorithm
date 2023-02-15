const fs = require("fs");
const filepath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filepath).toString().trim().split("\n");

const [N, M] = input.shift().split(" ").map(Number);
const graph = Array.from({ length: M }, () => []);
const visited = Array.from({ length: M }, () => Array(N).fill(false));

// for (let i = 0; i < M; i++) {
//   for (let j = 0; j < N; j++) {
//     graph[i].push(input[i][j]);
//   }
// }

for (let i = 0; i < input.length; i++) {
  graph[i] = input[i].trim().split("");
}

let dx = [1, 0, -1, 0];
let dy = [0, -1, 0, 1];

let white = 0;
let blue = 0;

function bfs(x, y, color) {
  let queue = [[x, y]];
  let count = 1;
  visited[x][y] = true;

  while (queue.length) {
    let [x, y] = queue.shift();
    for (let i = 0; i < 4; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];
      if (0 <= nx && nx < M && 0 <= ny && ny < N) {
        if (graph[nx][ny] == color && visited[nx][ny] == false) {
          count += 1;
          visited[nx][ny] = true;
          queue.push([nx, ny]);
        }
      }
    }
  }
  return count;
}

for (let p = 0; p < M; p++) {
  for (let q = 0; q < N; q++) {
    if (visited[p][q] == false) {
      if (graph[p][q] == "W") {
        white += bfs(p, q, "W") ** 2;
      } else {
        blue += bfs(p, q, "B") ** 2;
      }
    }
  }
}

console.log(white, blue);
