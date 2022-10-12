import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N, M = map(int, input().split())

adj = [[0] * (M + 1)] + [[0] + list(map(int, input().strip())) for _ in range(N)]

visited = [[0] * (M + 1) for _ in range(N + 1)]

def bfs(x, y) :

    dx = [0, 1, 0, -1]  # 왼쪽 아래쪽 오른쪽 위쪽
    dy = [-1, 0, 1, 0]  # 왼쪽 아래쪽 오른쪽 위쪽

    que =deque()
    que.append((x, y))
    visited[x][y] = 1           # list 자료형은 전역 변수 재선언 없이 사용 가능

    while que :

        x, y = que.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx > N or ny > M :
                pass            # if elif로 분기를 생성하였으므로 pass 가능 (4ms 단축...)
                                # if if의 경우 continue
            elif adj[nx][ny] == 1 and visited[nx][ny] == 0 :    # 인접 행렬의 요소가 1인 것을 기준으로 방문 처리도 가능
                adj[nx][ny] = adj[x][y] + 1
                que.append((nx, ny))
                visited[nx][ny] = 1

    return adj[N][M]

print(bfs(1,1))

# 최단 거리 문제

# dfs, deque, brute force