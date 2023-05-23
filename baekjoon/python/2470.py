import sys

sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())

pv_list = list(map(int, sys.stdin.readline().split()))

pv_list.sort()

# 투 포인터
start = 0
end = n - 1
# 초기값 설정
pv_abs = abs(pv_list[start] + pv_list[end])
res = [pv_list[start], pv_list[end]]

while start < end :

    pv_sum = pv_list[start] + pv_list[end]
    # 문제 조건에 따라 업데이트
    if abs(pv_sum) < pv_abs :
        pv_abs = abs(pv_sum)
        res = [pv_list[start], pv_list[end]]
    # 합이 0과 가깝게 하기 위해서
    if pv_sum > 0 :
        end = end - 1

    else :
        start = start + 1

print(*res)

# 이분 탐색 풀이도 해보자!