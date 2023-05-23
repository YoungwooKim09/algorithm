import sys

from queue import PriorityQueue

sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())
i = 0
que = PriorityQueue()

for _ in range(n) :
    order = int(sys.stdin.readline())

    if order == 0 :
        if que :
            print(que.get()[1]) # 튜플에 대한 index

        else :
            print(0)

    else :
        que.put((-order, order)) # 기본적으로 min heap 구조인 heapq 모듈의 응용

# 예외 처리에 있어서 try - except 구문 사용해보기
# heapq.heappush(heap, -num)
# print(-1 * heapq.heappop(heap))
# max hip 직접 구현해보기(while문 / 재귀), heap = []에서 시작하는 것 또한 고려

################################ Solution 1 ################################
# import sys, heapq

# n = int(sys.stdin.readline())
# i = 0
# heap = []

# for _ in range(n) :
#     order = int(sys.stdin.readline())

#     if order == 0 :
#         if heap :
#             print(heapq.heappop(heap)[1])

#         else :
#             print(0)

#     else :
#         heapq.heappush(heap, (-order, order))