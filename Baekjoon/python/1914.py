import sys

sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.read())

print(2 ** n - 1) # 반복 시행을 통해 찾은 규칙성

def move(n, x, y) :
        
    if n > 1 :
        move(n - 1, x, 6 - x - y)

    print(x, y)

    if n > 1 :
        move(n - 1, 6 - x - y, y)

if n <= 20 :
    move(n, 1, 3)