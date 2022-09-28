import sys

sys.stdin = open('input.txt', 'r')

num = int(sys.stdin.readline())

def factorial (num) : 

    if num > 0 :

        return num * factorial(num - 1)

    return 1

print(factorial(num))