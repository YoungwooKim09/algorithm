import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N, M = map(int, input().split())

stone = set()

for _ in range(N) :
    stone.add(input())

dp = [[float('inf')] * (int((2 * N) ** 0.5) + 2) for _ in range(N + 1)]         # 점화식 모든 항에 대해 공통적으로 적용 and 인덱스 편의성
                                                                                # 최소 횟수 갱신을 위해 무한대로 초기화
dp[1][0] = 0                                                                    # 초기값 설정

for i in range(2, N + 1) :
    if i in stone :                                                             # 'in'을 쓸 때 set 자료형이면 빠름
        continue
    for v in range(1, int((2 * i) ** 0.5) + 1) :                                # IndexError 방지를 위해 v - 1 번째 요소까지 검사
        dp[i][v] = min(dp[i - v][v - 1], dp[i - v][v], dp[i - v][v + 1]) + 1

if min(dp[N]) == float('inf') :
    print(-1)
else :
    print(min(dp[N]))

# 특정 돌에 특정 칸 수(v)로 점프하는 경우를 가정
# (i - v) 돌에서 특정 칸수(v)로 점프 할 수 있는 경우의 수 생각
# 최소 점프 횟수로 온 경우 + 1 (한번 뛰었다는 의미)
# 각각의 돌에 점프 간격에 따른 최소 점프 횟수가 저장되어 나감
# i에 따라 v의 범위를 유동적으로 설정할 수 있고, 이를 통해 시간 복잡도의 크기를 줄일 수 있다.
# 임의의 돌에 최소의 점프 횟수로 갈 수 있는 상황을 가정하고, 이를 통해 규칙성을 찾는다.
# N의 범위를 부등식을 통해 나타낼 수 있다.