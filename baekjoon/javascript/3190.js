const fs = require("fs");
const filepath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filepath).toString().trim().split("\n");

const N = Number(input.shift());
const K = Number(input.shift());

const arr = Array.from({ length: N }, () => Array.from({ length: N }, () => 0));
const rotations = new Map();

const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];

for (let i = 0; i < K; i++) {
    let [row, col] = input[i].split(" ").map(Number);
    arr[row - 1][col - 1] = 2;
}

for (let i = 0; i < input[K]; i++) {
    let [time, dir] = input[K + i + 1].split(" ");
    rotations.set(Number(time), dir === "L" ? 3 : 1);
}


class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}


class Queue {
    constructor() {
        this.size = 0;
        this.head = null;
        this.tail = null;
    }

    enqueue(value) {
        const node = new Node(value);

        if (!this.size) {
            this.head = node;
            this.tail = node;
        }
        else {
            this.head.next = node;
            this.head = node;
        }
        this.size++;
    }

    dequeue() {
        if (!this.size) return null;

        const deletedNodeValue = this.tail.value;

        if (this.size === 1) {
            this.head = null;
            this.tail = null;
        }
        else {
            this.tail = this.tail.next;
        }
        this.size--;

        return deletedNodeValue;
    }
}


const snake = new Queue();
snake.enqueue([0, 0]);
// const snake = [[0, 0]];
// let tailIndex = 0;

let curDir = 0;
let time = 0;

while (true) {
    time++;

    const [x, y] = snake.head.value;
    // const [x, y] = snake[snake.length - 1];
    const [dx, dy] = directions[curDir];
    const nx = x + dx;
    const ny = y + dy;

    if (nx < 0 || nx >= N || ny < 0 || ny >= N || arr[nx][ny] === 1) break;

    if (!arr[nx][ny]) {
        // 꼬리가 아닌 칸 초기화
        const [tx, ty] = snake.dequeue();
        // const [tx, ty] = snake[tailIndex];
        arr[tx][ty] = 0;
        // tailIndex++;
    }

    // 사과 유무와 관계 없이 뱀의 진행 과정 수행
    snake.enqueue([nx, ny]);
    // snake.push([nx, ny]);
    arr[nx][ny] = 1;
    
    // 해당 시간에 대한 회전이 정의되어 있을 때
    curDir = (curDir + (rotations.get(time) ?? 0)) % 4;
}

console.log(time);