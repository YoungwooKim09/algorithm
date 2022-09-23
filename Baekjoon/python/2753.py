import sys

sys.stdin = open('input.txt', 'r')

year = int(input())

if year % 4 == 0 and year % 100 != 0 :
    print('1')

elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0 :
    print('1')

else :
    print('0')