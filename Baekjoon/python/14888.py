import sys
from itertools import permutations

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

# # Brute force

# N = int(input())

# num = list(map(int, input().split()))

# op_num = list(map(int, input().split()))
# op_list = ['+', '-', '*', '/']
# op = []

# for i in range(len(op_num)) :
#     for _ in range(op_num[i]) :
#         op.append(op_list[i])

# maximum = -1e9
# minimum = 1e9       # 1 * 10^9 (10억)

# def cal():
#     global maximum, minimum

#     for case in permutations(op, N - 1) :

#         res = num[0]

#         for j in range(N - 1) :
#             if case[j] == '+' :
#                 res += num[j + 1]

#             elif case[j] == '-' :
#                 res -= num[j + 1]

#             elif case[j] == '*' :
#                 res *= num[j + 1]

#             else :
#                 res = int(res / num[j + 1]) # // (floor division) : 바닥 함수 - x를 넘지 않는 최대의 정수

#         if res >= maximum :
#             maximum = res   # 최대값 갱신

#         if res <= minimum :
#             minimum = res   # 최소값 갱신

# cal()
# print(maximum)
# print(minimum)

# dfs

N = int(input())

num = list(map(int, input().split()))

op = list(map(int, input().split()))

maximum = -1e9
minimum = 1e9

def dfs(count, res, plus, minus, multiply, divide):

    global maximum, minimum             # global 키워드를 사용하여 전역 변수 재선언

    if count == N:
        maximum = max(res, maximum)     # 최대값 Update
        minimum = min(res, minimum)     # 최소값 Update
        return

    # 각 연산자를 출발점으로 하여 연산 시작 - 트리 구조로 재귀 함수가 호출됨
    if plus :
        dfs(count + 1, res + num[count], plus - 1, minus, multiply, divide)
        
    if minus :
        dfs(count + 1, res - num[count], plus, minus - 1, multiply, divide)

    if multiply :
        dfs(count + 1, res * num[count], plus, minus, multiply - 1, divide)

    if divide :
        dfs(count + 1, int(res / num[count]), plus, minus, multiply, divide - 1)

dfs(1, num[0], op[0], op[1], op[2], op[3])

print(maximum)
print(minimum)