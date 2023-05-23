import sys

sys.stdin = open('input.txt', 'r')

temp = sys.stdin.read().splitlines()

testcase_num = temp[0]
testcase = list(map(int, temp[1].split()))
count = 0

for i in range(int(testcase_num)) :
    
    if   testcase[i] == 1 :
            count = count # 1은 소수가 아님

    elif testcase[i] == 2 :
            count = count +1

    else :
        # 소수 판별 반복문 시작
        for j in range(2, testcase[i]) :

            if testcase[i] % j == 0 : 
                count = count
                break

            else :
                if j == testcase[i] - 1 and testcase[i] % j != 0 :   
                    count = count + 1 # for loop가 끝까지 수행되었을 때

print(count)

# for one_of_testcase in testcase :
#     print(one_of_testcase)