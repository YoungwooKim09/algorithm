import sys

sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())

top = list(map(int, sys.stdin.readline().split()))

stk = []
res = []

for i in range(n) :

    while stk :

        if stk[-1][1] > top[i] :
            res.append(stk[-1][0] + 1)
            break

        else :
            stk.pop()

    if not stk :
        res.append(0)

    stk.append([i, top[i]])

print(*res)

# 스택으로 구현하여 시간 복잡도를 줄일 수 있다.