import sys

from itertools import product

sys.stdin = open('input.txt', 'r')

t = int(sys.stdin.readline()) # 테스트 케이스 갯수
arr = [1, 2, 3]

for _ in range(t) : # 테스트 케이스 갯수만큼 반복
    count = 0
    n = int(sys.stdin.readline()) # 정수 n
    for i in range(1, n + 1) :
            productLists = list(product(arr, repeat=i))
            for productList in productLists :
                if sum(productList) == n :
                    count = count + 1

    print(count)

# t = int(sys.stdin.readline())

# buff = [0] * 11

# buff[1] = 1
# buff[2] = 2
# buff[3] = 4


# for i in range(4, 11) :
#     buff[i] = buff[i-1] + buff[i-2] + buff[i-3]

# for _ in range(t) :
#     n = int(sys.stdin.readline())
#     print(buff[n])