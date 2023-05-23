import sys

from collections import deque

sys.stdin = open('input.txt', 'r')

n, k = list(map(int, sys.stdin.readline().split()))

que = deque([i for i in range(1, n + 1)])
res = []

while que :

    for _ in range(1, k) :
        num1 = que.popleft()
        que.append(num1)

    num2 = que.popleft()
    res.append(num2)

print('<' + str(res)[1:-1] + '>')