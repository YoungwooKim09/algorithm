const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let info = null;
let data = [];
let count = 0;

rl.on("line", function (line) {
  if (!info) {
    info = line.split(" ").map(Number);
  } else {
    data.push(line.split(" ").map(Number));
    count += 1;
  }
  if (count == 2) {
    rl.close();
  }
}).on("close", function () {
  let [N, M] = info;
  let a = data[0];
  let b = data[1];
  let sortedArr = [];

  let aPoint = 0;
  let bPoint = 0;

  while (aPoint < N && bPoint < M) {
    if (a[aPoint] > b[bPoint]) {
      sortedArr.push(b[bPoint++]);
    } else {
      sortedArr.push(a[aPoint++]);
    }
  }

  if (aPoint == N) {
    sortedArr = [...sortedArr, ...b.slice(bPoint)];
    console.log(sortedArr.join(" "));
  } else {
    sortedArr = [...sortedArr, ...a.slice(aPoint)];
    console.log(sortedArr.join(" "));
  }
  process.exit();
});
