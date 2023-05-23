import sys

from collections import deque

sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())
que = deque() # list 형

for _ in range(n) :
    order = sys.stdin.readline().split()
    
    if order[0] == 'push' :
        que.append(int(order[1]))

    elif order[0] == 'pop' :
        if not que :
            print(-1)
        else :
            num = que.popleft() # 시간 복잡도 O(1)
            print(num)          # pop(0)의 경우 시간 복잡도 O(n)

    elif order[0] == 'size' :
        print(len(que))

    elif order[0] == 'empty' :
        if que :
            print(0)

        else :
            print(1)

    elif order[0] == 'front' :
        if not que :
            print(-1)

        else :
            print(que[0])

    else :
        if not que :
            print(-1)

        else :
            print(que[-1])