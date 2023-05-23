import sys

sys.stdin = open('input.txt', 'r')

num = int(input())

for i in range(1, 10) :
    print(str(num)+" * "+str(i)+" = "+str(num * i))