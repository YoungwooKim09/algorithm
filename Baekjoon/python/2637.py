import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

needs = [[0] * (N + 1) for _ in range(N + 1)]

indegree = [0] * (N + 1)

for _ in range(M) :
    X, Y, K = map(int, input().split())

    graph[Y].append((X, K))                     # 가중치와 함께 저장
    indegree[X] += 1


def tropology_sort() :

    que = deque()

    for i in range(1, N + 1) :
        if indegree[i] == 0 :
            que.append(i)

    while que :
        now = que.popleft()
        
        for next, next_need in graph[now] :
            
            if needs[now].count(0) == N + 1 :               # now - 기본 부품
                needs[next][now] += next_need

            else :
                for j in range(1, N + 1) :                  # now - 중간 부품
                    needs[next][j] += needs[now][j] * next_need

            indegree[next] -= 1

            if indegree[next] == 0:
                que.append(next)

tropology_sort()

for k in enumerate(needs[N]) :                              # (index, element)의 형태로 반환
    if k[1] > 0 :                                           # element > 0
        print(*k)