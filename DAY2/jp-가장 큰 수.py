def solution(numbers):
    # 앞 세자리를 비교하여 정렬: 문자열*3 으로 내림차순 정렬
    li = sorted(list(map(str, numbers)), key = lambda x:x*3, reverse=True)

    # 각 숫자 이어붙여 반환 ("000" 위해 int 선변환)
    return str(int(''.join(li)))