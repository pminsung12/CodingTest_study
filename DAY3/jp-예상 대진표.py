def solution(n, a, b):
    cnt = 0

    # 다음순번 : 현재순번을 2로나눈 몫 + 나머지
    # a == b 일 때 break
    while a != b:
        a, b = (a // 2) + (a % 2), (b // 2) + (b % 2)
        cnt += 1
    return cnt
