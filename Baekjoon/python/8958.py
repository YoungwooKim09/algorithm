import sys

sys.stdin = open('input.txt', 'r')

var = sys.stdin.read().splitlines()

testcase_num = int(var[0])

for i in range(1, testcase_num+1) :

    testcase = var[i]

    score_list = []

    for j in range(len(testcase)) :

        if j == 0 :

            if testcase[j] == "O" :
                score = 1
                score_list.append(score)

            elif testcase[j] == "X" :
                score = 0
                score_list.append(score)

        else :

            if testcase[j] == "O" :
                score = 1
                
                if testcase[j] == testcase[j-1] :
                    score = score_list[j-1] + 1

                score_list.append(score)

            elif testcase[j] == "X" :
                score = 0
                score_list.append(score)

    print(sum(score_list))