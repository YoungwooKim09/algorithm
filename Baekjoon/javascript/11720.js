const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (N, nums) => {
  let sum = 0;
  for (let i = 0; i < N; i++) {
    sum += nums[i];
  }
  // const sum = nums.reduce((acc, cur) => acc + cur);
  console.log(sum);
};

let N = null;
let nums = null;
let count = 0;

rl.on("line", function (line) {
  if (!N) {
    N = parseInt(line);
  } else {
    nums = line.split("").map(Number);
  }
  count++;
  if (count == 2) {
    rl.close();
  }
}).on("close", function () {
  solution(N, nums);
  process.exit();
});
