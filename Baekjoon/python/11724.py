import sys
sys.setrecursionlimit(10**6)

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

visited = [0] * (N + 1)

for _ in range(M) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)      # 무방향 그래프

count = 0

def dfs(k) :

    visited[k] = 1    

    for i in graph[k] :
        if not visited[i] :
            dfs(i)

for j in range(1, N + 1) :
    if not visited[j] :     # 방문하지 않은 노드를 기준으로 DFS 
        dfs(j)
        count += 1

print(count)