from sys import stdin

stdin = open('input.txt', 'r')

input = stdin.readline

N = int(input())

INF = int(1e9)

graph = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (1<<N) for _ in range(N)]

def dfs(x, visited) :

    if visited == (1<<N) - 1 :
        if graph[x][0] :
            return graph[x][0]                                                          # base case
        else :
            return INF                                                                  # inf를 반환하면 min에서 자연스레 걸러진다

    if dp[x][visited] :                                                                 # dp에 저장되어 있음
        return dp[x][visited]

    dp[x][visited] = INF                                                                # 재귀가 호출되면서 해당 dp table INF으로 초기화

    for i in range(1, N) :                                                              
        if not graph[x][i] :                                                            # [1][1] = 0
            continue
        if visited & (1<<i) :                                                           # i가 이미 방문한 곳이라면
            continue                                                                    # visited의 i번째 인덱스가 1

        dp[x][visited] = min(dp[x][visited], dfs(i, (visited|(1<<i))) + graph[x][i])    # base case부터 저장해옴

    return dp[x][visited]

print(dfs(0, 1))                                                                        # cycle을 이루므로 출발 위치를 어디로 해도 같은 경로


# 비트 마스킹, DP, DFS
# 트리 구조를 그려서 구조화