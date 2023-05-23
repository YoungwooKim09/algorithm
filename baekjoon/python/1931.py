import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N = int(input())

time = [list(map(int, input().split())) for _ in range(N)]

# time.sort(key = lambda x : x[0])        # 가중치가 같으면 입력받은 순서대로 정렬
# time.sort(key = lambda x : x[1])        # 끝나는 시간이 같으면 시작 시간이 빠른 순서로 정렬되어야 함
#                                         # 따라서 시작시간이 빠른 순서대로 정렬한 후, 끝나는 시간이 빠른 순서대로 정렬   

time.sort(key = lambda x : (x[1], x[0]))  # 다중 조건 (우선 조건과 차선 조건) - x[1]을 기준으로 정렬할 때, 값이 같으면 x[0]을 기준으로 정렬

end = 0                                   # 첫 번째 시간에 대해서도 업데이트 하기 위해 초기값 설정
count = 0

for i, j in time :
    if i >= end :
        count += 1
        end = j

print(count)