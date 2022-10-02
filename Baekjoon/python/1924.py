import sys

sys.stdin = open('input.txt', 'r')

var = list(map(int, sys.stdin.read().split()))
x = var[0]
y = var[1]

daysList = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

diff = sum(daysList[:x]) + (y - 1)

result = day[diff % 7]

print(result)