import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

n = int(input())    # 노드의 개수
m = int(input())    # 간선의 개수

# 인접 리스트 (or 인접 행렬으로도 가능)
network = [[] for _ in range(n + 1)]

for _ in range(m) :
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

visited = [0] * (n + 1)

virus = []

# 순회 알고리즘(DFS or BFS)
def bfs(k) :

    que = deque([k])
    visited[k] = 1

    while que :
        res = que.popleft()
        virus.append(res)

        for i in network[res] :
            if not visited[i] :
                que.append(i)
                visited[i] = 1  # append할 때 방문 처리가 돼야 중복으로 추가가 안됨.
                
bfs(1)
print(len(virus) - 1)