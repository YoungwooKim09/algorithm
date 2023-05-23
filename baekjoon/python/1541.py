import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

nums = input().split('-')

for i in range(len(nums)) :
    x = nums[i].split('+')
    nums[i] = sum(map(int, x))

res = nums[0]

for j in range(1, len(nums)) :
    res -= nums[j]

print(res)