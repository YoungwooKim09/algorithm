import sys

sys.setrecursionlimit(10**6)

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

n = int(input())    # 노드의 개수

# 인접 리스트
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1) :
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [False] * (n + 1)
parent = [0] * (n + 1)

# dfs
def dfs(k) :
    visited[k] = True

    for i in tree[k] :
        if not visited[i] :
            parent[i] = k   # 부모 노드 체크
            dfs(i)

dfs(1)
print(*parent[2:], sep = '\n')