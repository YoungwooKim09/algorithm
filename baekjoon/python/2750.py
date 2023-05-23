import sys

sys.stdin = open('input.txt', 'r')

var = list(map(int, sys.stdin.read().splitlines()))

testcase_num = var[0]

var.remove(testcase_num)

for j in range(len(var)-1) : # Bubble sort
    for i in range(len(var)-1, j, -1) :
        if var[i] < var[i-1] :
            var[i], var[i-1] = var[i-1], var[i]

print(*var, sep = '\n')