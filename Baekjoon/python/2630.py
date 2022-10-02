import sys

sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())
arr = [list(map(int, input().split())) for _ in range(n)]

# res = 0

blue_count = 0
white_count = 0

def paper (x, y, n) : # 함수의 매개변수가 업데이트 되는 것을 유념

    global blue_count, white_count # 자료형의 특성 (list와 비교)

    for i in range(x, x + n) : # 시작 지점
        for j in range(y, y + n) : # 시작 지점
            if arr[x][y] != arr[i][j] : 
                paper(x, y, n//2)
                paper(x+(n//2), y, n//2)
                paper(x, y+(n//2), n//2)
                paper(x+(n//2), y+(n//2), n//2)
                return # 탈출 조건

    if arr[x][y] == 1 :
        blue_count = blue_count + 1

    else :
        white_count = white_count + 1



paper(0, 0, n)

print(white_count, blue_count, sep='\n')


# 같음과 다름의 비교에 있어서 직접적인 비교(=, !=)가 아닌 다른 방식 고려
# 요소의 '합'으로 접근

# a = [1, 2, 3, 4]

# if '3' in a :
#     print('True')

# 요소를 탐색할 때 다른 값을 찾았을 때 break를 이용하는 방법