import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

n = int(input())

for _ in range(n) :
    stk = []
    ptr = 0
    testcase = input().strip()
    
    for ps in testcase :
        
        if ps == '(' :
            stk.append('(')
            ptr = ptr + 1

        else :

            if stk == [] : # 빈 배열인지 확인하는 과정이 먼저 와야 함
                print('NO')
                break

            else :
                ptr = ptr - 1
                stk.pop(ptr)

    else :
        if stk == [] :
            print('YES')

        else :
            print('NO')