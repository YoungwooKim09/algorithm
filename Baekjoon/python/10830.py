import sys

sys.stdin = open('input.txt', 'r')

n, b = map(int, sys.stdin.readline().split())

input = sys.stdin.readline

mat = [list(map(int, input().split())) for _ in range(n)]

def mul_mat(mat1, mat2) :

    mat_square = [[0] * n for _ in range(n)]

    for row in range(n) :
        for col in range(n) :
            e = 0
            for i in range(n) :
                e += mat1[row][i] * mat2[i][col]
            mat_square[row][col] = e % 1000

    return mat_square

def power_mat(matrix, x) :
    if x == 1:
        return matrix

    elif x % 2 == 0 :
        tmp = power_mat(matrix, x // 2)
        return mul_mat(tmp, tmp)

    else :
        tmp = power_mat(matrix, x - 1)
        return mul_mat(mat, tmp)


res = power_mat(mat, b)

for j in res :
    for k in j :
        print(k % 1000, end = ' ')
    print()

# 자연수의 거듭제곱을 분할 정복으로 푸는 아이디어를 그대로 사용
# 단, 행렬의 거듭제곱이므로 행렬의 곱셈연산 함수를 정의