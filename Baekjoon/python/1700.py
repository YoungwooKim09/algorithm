import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N, K = map(int, input().split())

schedule = list(map(int, input().split()))

multitap = [0] * N

count = 0

for i in range(K) :

    k = 0

    if schedule[i] in multitap :
        continue

    elif 0 in multitap :
        multitap[multitap.index(0)] = schedule[i]
        continue

    else :
        for j in range(N) :
            if multitap[j] not in schedule[i:] :
                temp = multitap[j]
                break
            elif schedule[i:].index(multitap[j]) > k :
                temp = multitap[j]
                k = schedule[i:].index(multitap[j])

    multitap[multitap.index(temp)] = schedule[i]
    count += 1

print(count)

# 케이스를 분리해서 생각
# 꽂혀있는 것들 중 여러 개가 다시 사용될 때, 더 나중에 사용되는 것을 뽑는다 - 그리디적 사고
# 비교를 위해 k = 0 으로 초기화 후 이를 업데이트하는 형태로 진행