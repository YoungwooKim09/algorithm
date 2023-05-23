import sys

sys.stdin = open('input.txt', 'r')

testcase_info = list(map(int, sys.stdin.readline().split()))
n = testcase_info[0] # 테스트 케이스 갯수
m = testcase_info[1] # 필요한 나무

testcase = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(testcase)
res = 0

while start <= end :
    total = 0 # 들고갈 수 있는 나무
    mid = (start + end ) // 2

    for tree in testcase :
        if tree > mid :
            total = total + (tree - mid)

    if total >= m :
        res = mid
        start = mid + 1

    else :
        end = mid - 1

print(res)

# if total >= m , print(end)

# '적어도' M미터의 나무, 높이의 '최댓값'