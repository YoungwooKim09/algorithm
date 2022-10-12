import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

indegree = [0] * (N + 1)

for _ in range(M) :
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

res = []

def topology_sort() :
    
    que = deque()

    for i in range(1, N + 1) :
        if indegree[i] == 0 :
            que.append(i)

    while que :
        now = que.popleft()
        res.append(now)

        for j in graph[now] :
            indegree[j] -= 1
            if indegree[j] == 0 :
                que.append(j)

topology_sort()
print(*res)