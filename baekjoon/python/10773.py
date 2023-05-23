import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

n = int(input())
stk = []
ptr = 0

for i in range(n) :
    tmp = int(input())

    if tmp != 0 :
        stk.append(tmp)
        ptr = ptr + 1

    else :
        ptr = ptr - 1
        stk.pop(ptr)

print(sum(stk))