let N = 5;
let K = 3;
let array = [5, 10, 15, 20, 25];

// for (let i = 0; i < N - K + 1; i++) {
//     let sum = 0;
//     for (let j = 0; j < K; j++) {
//         sum += array[i + j];
//     }
//     console.log(sum);
// }

let sum = 0;
let cnt = 0;

for (let i = 0; i < N; i++) {
    sum += array[i];
    cnt++;
    if (cnt >= K) {
        console.log(sum);
        sum -= array[i - K + 1];
    }
}