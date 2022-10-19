import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]

res = 0

# needs = []

# for coin in coins :
#     if coin <= K :
#         needs.append(coin)

# for j in reversed(range(len(needs))) :
#     res += K // needs[j]
#     K %= needs[j]

# print(res)

for i in reversed(range(N)) :
    if K >= coins[i] :
        res += K // coins[i]
        K %= coins[i]

        if K == 0 :
            break

print(res)

# 그리디 알고리즘의 경우 정당성 분석이 중요
# 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로
# 작은 단위의 동전들을 종합해 다른 해가 나올 수 없음

# 그리디 알고리즘 문제 - 문제 풀이를 위한 최소한의 아이디어, 그것에 대한 정당성 검토
# 극단적인 조건을 토대로 문제에 접근한다는 점에서 정렬 기법이 함께 사용되는 경우가 많음