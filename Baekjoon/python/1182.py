import sys

from itertools import combinations

sys.stdin = open('input.txt', 'r')

testcase_info = sys.stdin.read().splitlines()

testcase_num = list(map(int, testcase_info[0].split()))[0]
testcase_sum = list(map(int, testcase_info[0].split()))[1]
testcase = list(map(int, testcase_info[1].split()))

count = 0

for i in range(1, len(testcase) + 1) :
    partitionList = list(combinations(testcase, i))
    for partition in partitionList :
        if sum(partition) == testcase_sum :
            count = count + 1

print(count)