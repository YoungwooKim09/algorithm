import sys

sys.stdin = open('input.txt', 'r')

temp = list(map(int, sys.stdin.read().splitlines()))

testcase_num = temp[0]

temp.remove(testcase_num)

for j in range(len(temp) - 1) :
    for i in range(j + 1, len(temp)) :
        if temp[j] > temp[i] :
            temp[j], temp[i] = temp[i], temp[j]

print(temp)