const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let cardInfo = null;
let cards = null;
let count = 0;

rl.on("line", function (line) {
  if (!cardInfo) {
    cardInfo = line.split(" ").map(Number);
  } else {
    cards = line.split(" ").map(Number);
    count += 1;
  }
  if (count == 1) {
    rl.close();
  }
}).on("close", function () {
  let [N, M] = cardInfo;
  let sum = 0;
  let max = 0;

  for (let i = 0; i < N - 2; i++) {
    for (let j = i + 1; j < N - 1; j++) {
      for (let k = j + 1; k < N; k++) {
        sum = cards[i] + cards[j] + cards[k];

        if (sum == M) {
          max = sum;
          break;
        } else if (sum < M) {
          max = Math.max(max, sum);
        }
      }
    }
  }
  console.log(max);
  process.exit();
});
