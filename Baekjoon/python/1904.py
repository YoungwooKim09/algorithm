import sys

sys.setrecursionlimit(10**6)

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N = int(input())

# # 탑다운 다이나믹 프로그래밍 - 시간 or 메모리 초과
# d = [0] * (N + 1)

# def tile(x) :
#     if x == 1 :
#         return 1

#     if x == 2 :
#         return 2

#     if d[x] != 0 :
#         return d[x]

#     d[x] = ((tile(x - 2)) + (tile(x - 1))) % 15746

#     return d[x]

# print(tile(N))


# 바텀업 다이나믹 프로그래밍
d = [0] * (N + 1)

d[1] = 1
d[2] = 2

for i in range(3, N + 1) :
    d[i] = (d[i - 1] + d[i - 2]) % 15746

print(d[N])