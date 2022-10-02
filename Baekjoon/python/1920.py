import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

n = int(input())

n_list = sorted(map(int, input().split())) # sort() 대신

m = int(input())

m_list = list(map(int, input().split()))

for i in range(m) :

    start = 0               # while문 종료 후 for문 진입 시 start와 end 초기화
    end = len(n_list) - 1   # while문 종료 후 for문 진입 시 start와 end 초기화

    while start <= end :

        mid = (start + end) // 2

        if m_list[i] > n_list[mid] :
            start = mid + 1

        elif m_list[i] == n_list[mid] :
            print(1)
            break

        else :
            end = mid - 1

    else: 
        print(0)