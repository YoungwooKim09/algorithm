import sys

sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())

stk = []
ptr = 0

for _ in range(n) :
    order = sys.stdin.readline().split()
    
    if order[0] == 'push' :
        stk.append(int(order[1]))
        ptr = ptr + 1

    elif order[0] == 'pop' :

        if stk == [] :
            print(-1)
            
        else :
            ptr = ptr - 1
            ele = stk.pop(ptr)
            print(ele)

    elif order[0] == 'size' :
        print(len(stk))

    elif order[0] == 'empty' :
        if stk == [] :
            print(1)
        
        else :
            print(0)

    else : 
        if stk == [] :
            print(-1)
        
        else :
            print(stk[ptr - 1])

    # for else와 break 대신 함수를 정의하여 return