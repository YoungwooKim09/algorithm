# import sys
# from collections import deque

# sys.stdin = open('input.txt', 'r')

# input = sys.stdin.readline

# N, M, K, X = map(int, input().split())

# route = [[] for _ in range(N + 1)]

# for _ in range(M) :
#     A, B = map(int, input().split())
#     route[A].append(B)

# visited = [0] * (N + 1)

# res = []

# def bfs(k) :

#     que = deque([k])
#     visited[k] = 1

#     while que :
#         std = que.popleft()

#         for i in route[std] :                   # for loop로 인접한 요소들에 대해 거리 계산
#             if not visited[i] :
#                 que.append(i)
#                 visited[i] = visited[std] + 1   # visited를 이용하여 각 노드까지의 거리 계산

#                 if visited[i] == K + 1 :
#                     res.append(i)

#     if not res :
#         res.append(-1)
                    
# bfs(X)
# res.sort()
# print(*res, sep = '\n')

import sys, heapq

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]

INF = int(1e9)

distance = [INF] * (N + 1)

for _ in range(M) :
    A, B = map(int, input().split())
    graph[A].append((B, 1))

def dijkstra(start) :
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0

    while que :
        new_distance, current = heapq.heappop(que)
        
        if distance[current] < new_distance :
            continue

        for i in graph[current] :
            cost = new_distance + i[1]

            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(que, (cost, i[0]))

dijkstra(X)

res = []

for j in range(1, N + 1) :
    if distance[j] == K :
        res.append(j)

if not res :
    print(-1)

else :
    for k in res :
        print(k, end = '\n')