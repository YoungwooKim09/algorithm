import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

# # 2차원 DP Table
# T = int(input())

# for _ in range(T) :
#     N = int(input())

#     coins = list(map(int, input().split()))
#     coins.insert(0, 0)

#     M = int(input())

#     d = [[0] * (M + 1) for _ in range(N + 1)]

#     for i in range(N + 1) :
#         d[i][0] = 1

#     for j in range(1, N + 1) :
#         for k in range(1, M + 1) :
#             d[j][k] = d[j - 1][k]

#             if k >= coins[j] :
#                 d[j][k] += d[j][k - coins[j]]

#     print(d[N][M])

# 1차원 DP Table
T = int(input())

for _ in range(T) :
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    d = [0] * (M + 1)

    d[0] = 1

    for coin in coins :
        for i in range(M + 1) :
            if i >= coin :
                d[i] += d[i - coin]

    print(d[M])