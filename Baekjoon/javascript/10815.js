const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function mergeSort(array) {
  if (array.length < 2) {
    return array;
  }
  const mid = Math.floor(array.length / 2);
  const left = array.slice(0, mid);
  const right = array.slice(mid);

  return merge(mergeSort(left), mergeSort(right));
}

function merge(left, right) {
  const result = [];
  let leftIndex = 0;
  let rightIndex = 0;
  // shift() 대신 투 포인터
  while (leftIndex < left.length && rightIndex < right.length) {
    if (left[leftIndex] < right[rightIndex]) {
      result.push(left[leftIndex]);
      leftIndex++;
    } else {
      result.push(right[rightIndex]);
      rightIndex++;
    }
  }
  return [...result, ...left.slice(leftIndex), ...right.slice(rightIndex)];
}

let M = null;
let N = null;
let myList = null;
let findList = null;
let count = 0;

rl.on("line", function (line) {
  if (!N) {
    N = parseInt(line);
  } else if (!myList) {
    myList = line.split(" ").map(Number);
  } else if (!M) {
    M = parseInt(line);
  } else {
    findList = line.split(" ").map(Number);
  }
  count++;
  if (count == 4) {
    rl.close();
  }
}).on("close", function () {
  let result = [];
  mySortedList = mergeSort(myList);

  for (let i = 0; i < findList.length; i++) {
    let start = 0;
    let end = mySortedList.length - 1;
    let isFind = false;

    while (start <= end) {
      mid = parseInt((start + end) / 2);
      if (mySortedList[mid] == findList[i]) {
        isFind = true;
        break;
      } else if (mySortedList[mid] > findList[i]) {
        end = mid - 1;
      } else {
        start = mid + 1;
      }
    }
    if (isFind) {
      result.push(1);
    } else {
      result.push(0);
    }
  }
  console.log(result.join(" "));

  process.exit();
});
