const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (N, K, data) => {
  if (N <= K) {
    return 0;
  }

  data.sort((a, b) => a - b);

  let answer = 0;
  const diff = [];

  for (let i = 0; i < data.length - 1; i++) {
    diff[i] = data[i + 1] - data[i];
  }
  diff.sort((a, b) => b - a);

  for (let i = K - 1; i < diff.length; i++) {
    answer += diff[i];
  }

  return answer;
};

let N = null;
let K = null;
let data;
let count = 0;

rl.on("line", function (line) {
  if (!N) {
    N = parseInt(line);
  } else if (!K) {
    K = parseInt(line);
  } else {
    data = line.trim().split(" ").map(Number);
    count += 1;
  }
  if (count == 1) {
    rl.close();
  }
}).on("close", function () {
  console.log(solution(N, K, data));
  process.exit();
});
