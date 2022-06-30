from collections import defaultdict

def solution(clothes):
    answer = 0
    cnt=1
    li=[]
    temp=[]
    dic=defaultdict(list)
    for i in clothes:
        dic[i[1]].append(i[0])
    val=list(dic.values())
    
    for i in val:
        cnt*=(len(i)+1) #선택안하는거 포함 +1
        
    
    return cnt-1 #다 선택안하는거 -1

"""  모든 조합다구하기 케이스1만 시간초과남

from collections import defaultdict
from itertools import combinations

def solution(clothes):
    answer = 0
    cnt=1
    li=[]
    temp=[]
    dic=defaultdict(list)
    for i in clothes:
        dic[i[1]].append(i[0])
    val=list(dic.values())
    
    for i in range(2,len(dic)+1):
        temp=list(combinations(val,i))
        li.extend(temp)
    for t in li:
        for i in t:
            cnt*=len(i)
        answer+=cnt
        cnt=1
    
    answer+=len(clothes)
    return answer
"""