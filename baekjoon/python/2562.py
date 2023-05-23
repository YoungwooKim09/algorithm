import sys

sys.stdin = open('input.txt', 'r')

# numList = list(map(int, sys.stdin.read().splitlines()))
numList = sys.stdin.read().splitlines()
print(max(numList))

for i in range(len(numList)) :
    if numList[i] == max(numList) :
        print(i+1)