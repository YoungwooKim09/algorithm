import sys

from collections import deque # queue보다 deque가 시간 복잡도 측면에서 더 유리한 이유?

sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())

que = deque()

for i in range(1, n + 1) :
    que.append(i) # que = deque([i for i in range(1, n + 1)])으로 하는 것이 시간 복잡도의 크기를 좀 더 줄일 수 있다.

while len(que) != 1 :
    que.popleft()
    num = que.popleft()
    que.append(num)

print(*que) # index 참조뿐만 아니라 unpacking도 가능 : print(*que.queue)