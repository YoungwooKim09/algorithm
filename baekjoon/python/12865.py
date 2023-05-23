import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N, K = map(int, input().split())

items = [list(map(int, input().split())) for _ in range(N)]

d = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1) :
    weight, val = items[i - 1]
    for j in range(1, K + 1) :
        if j >= weight :
            d[i][j] = max(d[i - 1][j], d[i - 1][j - weight] + val)  # [i - 1] - 해당 물건을 넣었기 때문에 이를 제외하고 생각

        else :
            d[i][j] = d[i - 1][j]

print(d[N][K])