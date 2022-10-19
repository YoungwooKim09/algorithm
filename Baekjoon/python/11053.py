import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N = int(input())

a = list(map(int, input().split()))

d = [1] * N

for i in range(1, N) :
    for j in range(i) :
        if a[i] > a[j] :
            d[i] = max(d[i], d[j] + 1)  # a[i]보다 작은 수 중에서 LCS 최대값 + 1을 위해 탐색하며 갱신

print(max(d))

# 현재 위치 이전의 모든 수를 탐색해야 하므로 O(N^2)의 시간 복잡도를 가짐
# 이분 탐색을 통해 시간 복잡도를 O(NlogN)으로 줄일 수 있음

# # Binary Search

# import sys

# from bisect import bisect_left

# sys.stdin = open('input.txt', 'r')

# x = int(input())
# arr = list(map(int, input().split()))

# dp = [arr[0]]

# for i in range(x):
#     if arr[i] > dp[-1]:
#         dp.append(arr[i])
#     else:
#         idx = bisect_left(dp, arr[i])
#         dp[idx] = arr[i]

# print(len(dp))