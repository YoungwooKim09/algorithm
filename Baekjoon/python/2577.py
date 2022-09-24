import sys

sys.stdin = open('input.txt', 'r')

var = sys.stdin.read().splitlines()

a, b, c = map(int, var)
result = a*b*c

for i in range(10) :
    count = 0
    
    for j in range(len(str(result))) :
        if str(i) == str(result)[j] :
            count = count + 1
        
    print(count)