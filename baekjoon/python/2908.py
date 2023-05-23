import sys

sys.stdin = open('input.txt', 'r')

var = sys.stdin.read().split()
num1 = var[0][2]+var[0][1]+var[0][0]
num2 = var[1][2]+var[1][1]+var[1][0]

if int(num1) > int(num2) :
    print(num1)

else :
    print(num2)