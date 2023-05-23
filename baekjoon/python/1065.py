import sys

sys.stdin = open('input.txt', 'r')

num = sys.stdin.readline().strip()

def hanNum (num) :
    
    if int(num) <= 99 :
        
        count = num
        
    elif 100 <= int(num) <= 999 :
        
        count = 99

        for j in range(100, int(num)+1) :

            temp = list(map(int, str(j)))

            for i in range(1, len(temp) - 1) :
                if temp[i] - temp[i-1] == temp[i+1] - temp[i] :
                    count = count + 1

    else :
        count = hanNum (999)
        
    return count

print(hanNum (num))