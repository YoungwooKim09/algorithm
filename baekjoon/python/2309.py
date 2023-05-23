import sys

sys.stdin = open('input.txt', 'r')

totalHeights = list(map(int, sys.stdin.read().splitlines()))

sumHeights = sum(totalHeights)

#flag = 0

def chaewook (totalHeights) :

    for i in range(len(totalHeights)) :
        for j in range(len(totalHeights)) :
            if i != j and sumHeights - (totalHeights[i] + totalHeights[j]) == 100 : # '합'을 이용
                a = totalHeights[i]
                b = totalHeights[j]
                totalHeights.remove(a)
                totalHeights.remove(b)

                return totalHeights
        # if a:
        #     break
        
chaewook(totalHeights).sort() # None 반환

print(*totalHeights, sep='\n')

#call by value, call by reference