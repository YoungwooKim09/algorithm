import sys

sys.stdin = open('input.txt', 'r')

testcase = sys.stdin.readline().strip()

stk = []
tmp = 1
res = 0

for i in range(len(testcase)) :
    if testcase[i] == '(':
        stk.append(testcase[i])
        tmp = tmp * 2


    elif testcase[i] == '[' :
        stk.append(testcase[i])
        tmp = tmp * 3


    elif testcase[i] == ')' :
        if not stk or stk[-1] == '[':
            res = 0
            break

        elif testcase[i-1] == '(' : # 실행문의 조건을 testcase를 기준으로 정함
            res = res + tmp

        stk.pop() # 스택에서 이미 계산된 괄호에 대해서 pop
        tmp = tmp // 2


    else  : # pc == ']'
        if not stk or stk[-1] == '(': # 스택이 비어있거나 스택의 마지막 인덱스에 해당하는 값이 '('이면,
            res = 0
            break

        elif testcase[i-1] == '[' :
            res = res + tmp
        
        stk.pop()
        tmp = tmp // 3

if stk : # 만약 스택이 비어있지 않다면,
    res = 0

print(res)