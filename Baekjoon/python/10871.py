import sys

sys.stdin = open('input.txt', 'r')

var = sys.stdin.read().splitlines()
testcase_num, compare_num = map(int, var[0].split())

testcase_list = var[1].split()

result = []

for i in range(testcase_num) :
    if int(testcase_list[i]) < compare_num :
        result.append(testcase_list[i])

print(*result)