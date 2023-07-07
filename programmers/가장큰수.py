def solution(numbers):
    numbers_str = sorted([str(num) for num in numbers], key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers_str)))

# 각 자리수 별 문자에 대한 유니코드 비교
# 3은 33, 333과 동일
# 3은 31, 331보다 커야 한다.
# 따라서 3을 333으로 변환하여 비교
# [0, 0, 0]과 같은 예외 처리를 위한 형 변환(int)

# key를 통해 각 리스트 요소에 대해 호출할 함수 지정
# 해당 함수는 정렬 목적으로 사용할 키를 반환하는 함수여야 함