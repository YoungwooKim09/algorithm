import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N, M, V = map(int, input().split())

# graph = [[] for _ in range(N + 1)]

# for _ in range(M) :

#     a, b = map(int, input().split())

#     graph[a].append(b)
#     graph[b].append(a)            # 양방향 그래프

# for node in graph :
#     node.sort()

matrix = [[0] * (N + 1) for _ in range(N + 1)]

visited = [0] * (N + 1)

for _ in range(M) :
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1 # 양방향 그래프


def DFS(k) :
    visited[k] = 1
    print(k, end = ' ')

    for i in range(1, N + 1) :
        if visited[i] == 0 and matrix[k][i] == 1 :
            DFS(i)

    # for i in graph[k] :
    #     if not visited[i] :
    #         DFS(i)


def BFS(k) :
    que = deque([k])
    visited[k] = 0

    while que :
        res = que.popleft()
        print(res, end = ' ')

        for i in range(1, N + 1) :
            if visited[i] == 1 and matrix[res][i] == 1 :
                que.append(i)
                visited[i] = 0

        # for i in graph[k] :
        #     if not visited[i] :
        #         que.append(i)
        #         visited[i] = True

DFS(V)

print()

BFS(V)

# 인접 행렬과 인접 리스트 각각의 장점과 단점