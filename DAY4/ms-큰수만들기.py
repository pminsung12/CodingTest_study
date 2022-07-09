def solution(number, k):
    answer = []
    for i in number:
        if not answer:
            continue
        if k>0:
            while answer[-1] < num: # 리스트 맨뒤에꺼랑 다음꺼랑 비교
                answer.pop()
                k-=1
                if not answer or k<=0:
                    break
        answer.append(i)
    return ''.join(answer[:len(answer)-k]) #k가 남아있는 경우 뒤에서부터 제거
    



""" 시간초과
from itertools import combinations

def solution(number, k):
    answer = ''
    a=list(combinations(list(number),len(number)-k))
    return ''.join(sorted(a,reverse=True)[0])
"""