import sys
from itertools import permutations

sys.stdin = open('input.txt', 'r')

testcase_input = list(map(int, sys.stdin.read().splitlines()))

arr = testcase_input[2:]

cardLists = list(permutations(arr, testcase_input[1]))
result = set()

for cardList in cardLists :
    result.add("".join(list(map(str, cardList))))

print(len(result))

# for cardList in cardLists :
#     result.add("".join(cardList))

# print(result)

# def perm (arr, k) : 

#     def dac (arr) :

#         if len(arr) < 2 :
#             return [arr]

#         mid = len(arr) // 2

#         left_arr = dac(arr[:mid])
#         right_arr = dac(arr[mid:])

#         tmp = left_arr + right_arr
        
#         return tmp

#     # result = []
#     # for i in [1,2,12,1]:
#     #     result.append([i])

#     if k == 1 :
#         return dac(arr) # return이 없으면 단순히 'tmp'
        
#     result = []

#     # [i 실행할 구문 for i in 반복할 구간]
#     # [0 for i in range(5)]


#     for i in perm(arr, k - 1) : 
#         for j in arr :
#             seq = i + [j]
#             result.append(seq)

#     # flag 사용해서 중복 방지

#     return result

# print(perm(arr, 3))