import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    N = int(input())
    score = [list(map(int, input().split())) for _ in range(N)]
    score.sort(key = lambda x : x[0])
    
    top = score[0][1]
    count = 1

    for i in range(1, N) :
        if score[i][1] < top :
            count += 1
            top = score[i][1]    

    print(count)

# 비교를 위한 기준을 세우자 -> 서류 심사 성적을 기준으로 정렬
# 서류 심사 1등 지원자는 선발 - 다른 모든 지원자들과 비교했을 때 어느 하나의 성적(서류 심사 성적)이 항상 위이므로
# 서류 심사 2등의 지원자는 1등의 지원자보다 서류 성적이 낮으므로 선발되기 위해서는 면접 심사 성적이 더 높아야 함
# 마찬가지로 서류 심사 3등의 지원자는 서류 심사 1등, 2등의 지원자보다 면접 심사 성적이 높아야 함 - 다른 모든 지원자들과의 비교 과정 때문에
# 위 경우 1등, 2등의 지원자보다 면접 심사 성적이 높아야 하므로, 1등과 2등 지원자 성적 중 더 높은 면접 심사 성적보다 높아야 하는 것과 동일함
# 이전 사람들 중 가장 높은 면접 순위를 갱신하며 탐색하여 시간 복잡도를 줄여야 함