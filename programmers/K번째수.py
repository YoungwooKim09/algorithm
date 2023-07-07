def solution(array, commands):
    answer = []
    
#     for command in commands:
#         i = command[0]
#         j = command[1]
#         k = command[2]
#         sortedArr = sorted(array[i-1:j])
#         answer.append(sortedArr[k-1])
        
#     return answer

    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# map function으로 lambda 함수 사용
# 각 요소를 lambda 함수의 인수로 제공