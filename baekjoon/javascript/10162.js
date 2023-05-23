const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = "";
let buttons = [300, 60, 10];
let answer = [];

rl.on("line", function (line) {
  data = parseInt(line);
  rl.close();
}).on("close", function () {
  // 풀이 1)
  for (let i = 0; i < 3; i++) {
    // 해당 버튼을 누르지 않는 경우
    if (buttons[i] > data) {
      answer[i] = 0;
      continue;
    } else {
      let count = parseInt(data / buttons[i]);
      answer[i] = count;
      data -= buttons[i] * count;
    }
  }
  // T초를 맞출 수 없는 경우
  if (data) {
    console.log("-1");
  } else {
    console.log(answer.join(" "));
  }

  //   // 풀이 2)
  //   const bt1 = Math.floor(data / 300);
  //   const bt2 = Math.floor((data - 300 * bt1) / 60);
  //   const bt3 = Math.floor((data - 300 * bt1 - 60 * bt2) / 10);

  //   data - 300 * bt1 - 60 * bt2 - 10 * bt3 === 0
  //     ? console.log(`${bt1} ${bt2} ${bt3}`)
  //     : console.log("-1");

  process.exit();
});
