import sys

# sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline().split()[0])

# testcase = list(map(int, sys.stdin.read().splitlines()))[1:]

# buff = [0 for _ in range(max(testcase)+1)]

buff = [0]*10001

max_buff = 0

for _ in range(N):
    pre_num = int(sys.stdin.readline().split()[0])
    buff[pre_num] += 1      # buff[pre_num] = buff[pre_num] + 1
    if pre_num > max_buff:
        max_buff = pre_num

# for each in range(N) :
#     temp = sys.stdin().read
#     buff[each] = buff[each] + 1

for i in range(max_buff + 1) :
    for _ in range(buff[i]) :
        sys.stdout.write(str(i) + '\n')