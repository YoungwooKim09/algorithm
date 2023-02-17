const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let n = null;
let data = [];
let count = 0;

rl.on("line", function (line) {
  if (!n) {
    n = parseInt(line);
  } else {
    data.push(line.split("").map(Number));
    count += 1;
  }
  if (count == n) {
    rl.close();
  }
}).on("close", function () {
  let dx = [0, 1, 0, -1];
  let dy = [1, 0, -1, 0];

  let visited = Array.from({ length: n }, () =>
    Array.from({ length: n }, () => -1)
  );
  visited[0][0] = 0;
  let queue = [[0, 0]];

  while (queue.length) {
    let [x, y] = queue.shift();
    for (let i = 0; i < 4; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];

      if (0 <= nx && nx < n && 0 <= ny && ny < n) {
        // 방문하지 않은 경우
        if (visited[nx][ny] == -1) {
          // 흰 방
          if (data[nx][ny] == 1) {
            visited[nx][ny] = visited[x][y];
            queue.push([nx, ny]);
          }
          // 검은 방
          else {
            visited[nx][ny] = visited[x][y] + 1;
            queue.push([nx, ny]);
          }
        }
        // 방문한 경우
        else {
          // 흰 방
          if (data[nx][ny] == 1) {
            if (visited[nx][ny] > visited[x][y]) {
              visited[nx][ny] = visited[x][y];
              queue.push([nx, ny]); // ?? -> 다시 보기
            }
          }
          // 검은 방
          else {
            if (visited[nx][ny] > visited[x][y] + 1) {
              visited[nx][ny] = visited[x][y] + 1;
              queue.push([nx, ny]); // ?? -> 다시 보기
            }
          }
        }
      }
    }
  }
  console.log(visited[n - 1][n - 1]);
  process.exit();
});
