const fs = require("fs");
const filepath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const [, a, b] = fs.readFileSync(filepath).toString().trim().split("\n");

let sumArray = [...a.split(" ").map(Number), ...b.split(" ").map(Number)];
let answer = sumArray.sort((a, b) => a - b);

console.log(answer.join(" "));

// javascript sort(timsort)'s time complexity : nlog(n)