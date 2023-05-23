const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let N = null;

rl.on("line", function (line) {
  N = parseInt(line);
  rl.close();
}).on("close", function () {
  let M = 0;
  //   // for문
  //   for (let i = 1; i < N; i++) {
  //     let candidateValue = i;
  //     let stringValue = candidateValue.toString();

  //     let sum = candidateValue;

  //     for (let j = 0; j < stringValue.length; j++) {
  //       sum += parseInt(stringValue[j]);
  //     }
  //     if (sum == N) {
  //       M = candidateValue;
  //       break;
  //     }
  //   }

  // while문
  let candidateValue = 1;

  while (true) {
    // sum > N은 틀린 조건 : 89 -> 106, 90 -> 99
    if (candidateValue > N) {
      break;
    }

    let sum = candidateValue;
    let stringValue = candidateValue.toString();

    for (let i = 0; i < stringValue.length; i++) {
      sum += parseInt(stringValue[i]);
    }

    if (sum == N) {
      M = candidateValue;
      break;
    }

    candidateValue++;
  }

  console.log(M);
  process.exit();
});
