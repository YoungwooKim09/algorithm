import sys

sys.stdin = open('input.txt', 'r')

num = sys.stdin.readline()
star = "*"
for i in range(1, int(num)+1) :
    print(star*i)