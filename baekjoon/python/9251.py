import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

word1 = input().strip()
word2 = input().strip()

d = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]

for i in range(1, len(word2) + 1) :
    for j in range(1, len(word1) + 1) :
        if word1[j - 1] == word2[i - 1] :
            d[i][j] = d[i - 1][j - 1] + 1

        else :
            d[i][j] = max(d[i - 1][j], d[i][j - 1])

print(d[-1][-1])