import sys

sys.setrecursionlimit(10**6)

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

def dfs(k, color) :

    global check

    if not check:                       # check = False
        return

    visited[k] = color

    for i in graph[k] :                 # 인접 노드
        if not visited[i] :
            dfs(i, -color)

        elif visited[i] == visited[k] : # 인접 노드 간 같은 그룹
            check = False
            return

K = int(input())

for _ in range(K) :

    V, E = map(int, input().split())

    graph = [[] for _ in range(V + 1)]

    for _ in range(E) :
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [0] * (V + 1)
    
    check = True

    for j in range(1, V + 1) :
        if not visited[j] :
            dfs(j, 1)
        
            if not check:
                break

    print("YES" if check else "NO")

# check 변수가 아닌 boolean 자료형을 직접 return하는 방식으로 다시 구현해보기