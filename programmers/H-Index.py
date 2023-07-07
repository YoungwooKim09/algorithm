def solution(citations):
    # 오름차순 정렬 풀이
    citations.sort()
    citations_length = len(citations)
    
    for i in range(citations_length):
        if citations[i] >= citations_length - i:
            return citations_length - i
    
    return 0

    # # 내림차순 정렬 풀이
    # citations.sort(reverse=True)
    # citations_length = len(citations)
    
    # for i in range(citations_length):
    #     if citations[i] <= i:
    #         return i
        
    # return citations_length

# 정렬된 배열에서 인용 횟수와 논문의 수가 같은 지점이 기준이 된다.