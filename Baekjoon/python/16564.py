import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

n, k = map(int, input().split())

team = [int(input()) for _ in range(n)]

start = min(team)
end = min(team) + k

while start <= end :
    mid = (start + end) // 2
    total = 0

    for level in team :
        if mid - level > 0 :
            total = total + (mid - level)

    if total > k :
        end = mid - 1

    else :
        res = mid
        start = mid + 1

print(res)