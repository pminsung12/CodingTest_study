from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(information, queries):
    answer = []
    dic=defaultdict(list)
    for info in information:
        info=info.split()
        condition=info[:-1]#점수빼고 다
        score=int(info[-1])#점수
        #각 인덱스를 조합만들어서 -가 각자리에 다 들어가서 모든 조합을 만들 수 있게
        for i in range(5):
            case=list(combinations(range(4),i))#combinations([0,1,2,3],i)
            for c in case:
                tmp=condition.copy()
                for idx in c:
                    tmp[idx]="-"
                key=''.join(tmp)
                dic[key].append(score)#defaultdict니까 try except 예외처리 안해줌
    for value in dic.values():
        value.sort()
    for query in queries:
        query=query.replace("and","")#and제거
        query=query.split()#공백제거
        target_key=''.join(query[:-1])
        target_score=int(query[-1])
        count=0
        if target_key in dic:
            target_list=dic[target_key]
            idx=bisect_left(target_list, target_score)#정렬된 a에 x를 삽입할 위치를 리턴해준다. x가 a에 이미 있으면 기존 항목의 앞 (왼쪽)의 위치를 반환한다.
            count=len(target_list)-idx
        answer.append(count)
    
    return answer
"""시간초과
def solution(info, query):
    answer = []
    cnt=0
    for i in range(len(info)):
        info[i]=info[i].split()
    for i in range(len(query)):
        query[i]=query[i].split()
    
    for q in query:
        for i in info:
            if int(q[7])<=int(i[4]):
                if q[0]!='-' and q[0]!=i[0]:
                    continue
                if q[2]!='-' and q[2]!=i[1]:
                    continue
                if q[4]!='-' and q[4]!=i[2]:
                    continue
                if q[6]!='-' and q[6]!=i[3]:
                    continue
                
                cnt+=1
        answer.append(cnt)
        cnt=0
    
    return answer
"""