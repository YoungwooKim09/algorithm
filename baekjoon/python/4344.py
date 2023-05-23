import sys

sys.stdin = open('input.txt', 'r')

var = sys.stdin.read().splitlines()

testcase_num = var[0]

for i in range(1, len(var)) :
    testcase = var[i]
    
    testcase_list = list(map(int, testcase.split()))
    
    testcase_avg = round((sum(testcase_list)-testcase_list[0])/testcase_list[0], 3)
    
    count = 0

    for j in range(1,len(testcase_list)) :
        
        if testcase_list[j] > testcase_avg :
            count = count + 1

    rate = (count/(len(testcase_list)-1))*100

    print(f"{rate:.3f}%")