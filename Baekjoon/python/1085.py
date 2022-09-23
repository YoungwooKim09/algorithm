import sys

sys.stdin = open('input.txt', 'r')

x, y, w, h = map(int, input().split())

minRoute = min([x - 0, y - 0, w - x, h - y])

print(minRoute)