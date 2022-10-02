import sys

sys.stdin = open('input.txt', 'r')

tmp = sys.stdin.read().splitlines()

testcase_info = tmp[0]
testcase = list(map(int, tmp[1:]))
testcase.sort()

n, c = map(int, testcase_info.split())

start = 1 # 1이 최소값
end = testcase[-1] - testcase[0]

res = 0

while start <= end :

    mid = (start + end) // 2
    count = 1
    current = testcase[0]

    for i in range(1, n) :
        if testcase[i] - current >= mid : # i = 3 -> (i = 4) - (i = 3) 최소 간격보다 먼 곳에 설치 가능
            count = count + 1
            current = testcase[i] # 변수[index]는 업데이트 안됨!
        
    if count >= c :
        res = mid
        start = mid + 1

    else :
        end = mid - 1

print(res)

# 인접한 두 공유기의 '최대' 간격을 이분 탐색