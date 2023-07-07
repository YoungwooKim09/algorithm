from collections import Counter

def solution(v):
    answer = []

    for i in zip(*v):
        x = Counter(i)
        answer.extend([i for i in x if x[i] == 1])

    return answer

    # # XOR 연산을 이용한 풀이
    # return [v[0][0] ^ v[1][0] ^ v[2][0], v[0][1] ^ v[1][1] ^ v[2][1]]