import sys

sys.stdin = open('input.txt', 'r')

temp = sys.stdin.read().splitlines()


testcase_num = temp[0]


for i in range(1, len(temp)) :
    testcase = temp[i]
    iter = testcase.split()[0]
    testcase_str = testcase.split()[1]
    
    result = ''

    for j in range(len(testcase_str)) :
        
        P = testcase_str[j]*int(iter)
        result = result + P

    print(result)