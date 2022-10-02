import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
n = int(input())

# for _ in range(n) :
#     stick = int(sys.stdin.readline())
#     stk.append(stick)


stk = [int(input()) for _  in range(n)]
lim = stk.pop()
count = 1

for _ in range(n - 1) :
    ele = stk.pop()

    if ele > lim :
        count = count + 1
        lim = ele

print(count)