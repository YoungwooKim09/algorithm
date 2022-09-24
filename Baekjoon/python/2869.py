import sys, math

sys.stdin = open('input.txt', 'r')

var = list(map(int, sys.stdin.read().split()))

A = var[0]
B = var[1]
V = var[2]

days = 0

if (V - A) % (A - B) == 0 :
    days = (V - A) // (A - B) + 1
    print(days)

else :
    cal = math.ceil((V - A) / (A - B))
    days = cal + 1
    print(days)

# if V == A :
#     days = days + 1
#     print(days)

# else : 
#     while True :
#         days = days + 1

#         if A >= (V - days * (A - B)) :
#             days = days + 1
#             print(days)
#             break