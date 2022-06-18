#못품, 아이디어가 너무어렵네
def solution(numbers):
    #문자열을 3번씩 반복해서 비교하기 최소한자리이므로 최대 3자리를 맞추기위해서
    numbers=sorted(list(map(str,numbers)),key=lambda x:x*3, reverse=True)
    
    return str(int(''.join(numbers))) #000일 경우 000이 아니라 0이 출력되도록 함.

""" 노가다풀이 틀림
from functools import cmp_to_key
def compare(x,y):
    if x[0]>y[0]: 
        return -1
    elif x[0]==y[0]:
        if len(x)<len(y):
            for i in range(0,len(x)):
                if x[i]<y[i+1]:
                    return 1
                elif x[i]>y[i+1]:
                    return -1
                
        elif(len(x)==len(y)):
            for i in range(0,len(x)):
                if x[i]>y[i]:
                    return -1
                elif x[i]<y[i]:
                    return 1
        else :
            for i in range(0,len(y)):
                if y[i]<x[i+1]:
                    return -1
                elif y[i]>x[i+1]:
                    return 1
        return -1
            
    else:
        return 1


def solution(numbers):
    answer = ''
    numbers=list(map(str,numbers))
    numbers=sorted(numbers,key=cmp_to_key(compare))
    
    return ''.join(numbers)
"""