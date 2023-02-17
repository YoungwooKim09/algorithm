const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (num, data) => {
  let prime = Array.from({ length: MAX }, () => true);
  let visited = Array.from({ length: MAX }, () => 0);

  // 에라토스테네스의 체
  for (let j = 2; j <= Math.sqrt(MAX); j++) {
    // 소수가 아니므로 continue
    if (prime[j] == false) continue;
    // i * k (k < i)까지의 수는 이미 검사했으므로 j는 i * i부터 검사
    for (let k = j * j; k < MAX; k += j) {
      prime[k] = false;
    }
  }

  let start = data[num][0];
  let end = data[num][1];

  visited[start] = 1;
  let queue = [[start, 0]];

  while (queue.length) {
    let [now, cnt] = queue.shift();
    strNow = String(now);
    if (now == end) {
      return cnt;
    }
    for (let p = 0; p < 4; p++) {
      for (let q = 0; q < 10; q++) {
        let temp = parseInt(strNow.slice(0, p) + q + strNow.slice(p + 1, 4));
        if (visited[temp] == 0 && prime[temp] && temp >= 1000) {
          visited[temp] = 1;
          // 같은 변환 횟수로 큐에 들어가야 함
          queue.push([temp, cnt + 1]);
        }
      }
    }
  }
  return "impossible";
};

let T = null;
let MAX = 10000;
let data = [];
let count = 0;

rl.on("line", function (line) {
  if (!T) {
    T = parseInt(line);
  } else {
    data.push(line.split(" ").map(Number));
    count += 1;
  }
  if (count == T) {
    rl.close();
  }
}).on("close", function () {
  for (let num = 0; num < T; num++) {
    console.log(solution(num, data));
  }
  process.exit();
});
