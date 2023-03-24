const fs = require("fs");
const filepath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = parseInt(fs.readFileSync(filepath).toString());

// // solution 1
// let num = 1;
// let cnt = 0;

// while (num <= input) {
//     cnt++;
//     num = Math.pow(2, cnt);
// }

// const binary = Array.from({ length: cnt }, () => 0);

// let compareNum = input;
// for (let i = cnt - 1; i >= 0; i--) {
//     let temp = Math.pow(2, i);

//     if (temp === compareNum) {
//         binary[i] = 1;
//         break;
//     }

//     if (temp > compareNum) {
//         continue;
//     }

//     binary[i] = 1;
//     compareNum -= temp;
// }

// console.log(binary.reverse().join(''));

// // solution 2
// let num = input;
// let res = "";

// while (num != 0) {
//     res = (num % 2).toString() + res;
//     num = Math.floor(num / 2);
// }

// console.log(res);

// solution 3
let res = "";

function binary (num) {
    if (num === 0) return;

    binary(Math.floor(num / 2));
    res += num % 2;
}

binary(input);
console.log(res);