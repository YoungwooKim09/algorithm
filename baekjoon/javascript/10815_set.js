const [, ns, , ms] = require("fs")
  .readFileSync("./input.txt")
  .toString()
  .trim()
  .split("\n");
const myList = new Set(ns.split(" ").map(Number));
const findList = ms.split(" ").map(Number);
let result = [];

for (let card of findList) {
  result.push(myList.has(card) ? 1 : 0);
}
console.log(result.join(" "));

// Set의 has()는 O(1) - 해쉬 테이블로 구현
// Set은 Map 객체처럼 key를 가지고 있지 않지만,
// Map 객채와의 유사성을 위해([key, value] 형태를 위해)
// value와 동일한 key를 가진다.
