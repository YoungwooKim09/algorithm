import sys

sys.stdin = open('input.txt', 'r')

testcases = sys.stdin.readlines()

for i in range(1, len(testcases)) :
    only_testcases = testcases[i].strip()
    a, b = map(int, only_testcases.split())
    print(a+b)