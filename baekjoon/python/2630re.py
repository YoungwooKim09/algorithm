import sys

sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] # 2차원 배열을 만들어 좌표로 접근
res = []

def devideRecursion (x, y, n) :
    for i in range(x, x + n) :
        for j in range(y, y + n) :
            if arr[x][y] != arr[i][j] :
                devideRecursion(x, y, (n//2))
                devideRecursion(x+(n//2), y, (n//2))
                devideRecursion(x, y+(n//2), (n//2))
                devideRecursion(x+(n//2), y+(n//2), (n//2))
                return # if와 동일선상에 있을 때 함수가 조기종료

    if arr[x][y] == 1 :
        res.append(1)

    else :
        res.append(0)

devideRecursion(0, 0, n)

print(res.count(0), res.count(1), sep='\n')