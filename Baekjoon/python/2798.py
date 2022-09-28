import sys

sys.stdin = open('input.txt', 'r')

temp = sys.stdin.read().splitlines()
testcase_info = list(map(int, temp[0].split()))
testcase_num = testcase_info[0]
testcase_score = testcase_info[1]
testcase = list(map(int, temp[1].split()))

buff = []

def blackJack (testcase) :
    for i in range(len(testcase)) :
        for j in range(len(testcase)) :
            for k in range(len(testcase)) :

                if i != j and i != k and k != j and (testcase[i] + testcase[j] + testcase[k]) == testcase_score :
                    result = testcase_score
                    return result

                elif i != j and i != k and k != j and (testcase[i] + testcase[j] + testcase[k]) < testcase_score :
                    testcase_sum = testcase[i] + testcase[j] + testcase[k]
                    buff.append(testcase_sum)

    return max(buff)

print(blackJack (testcase))