# ref others, permu possible?, eval()?
from itertools import permutations

def operation(snum1, snum2, op):
    if op=='*':
        return str(int(snum1)*int(snum2))
    elif op=='+':
        return str(int(snum1)+int(snum2))
    elif op=='-':
        return str(int(snum1)-int(snum2))

def calculate(exp, op):#op는 순열 한 피스가 들어옴
    arr=[]
    tmp=""
    #arr에 숫자와 기호를 각각의 원소로 저장
    for i in exp:
        if i.isdigit()==True:
            tmp+=i
        else:
            arr.append(tmp)
            arr.append(i)
            tmp=""
    arr.append(tmp)
    
    for o in op:#1순위부터 3순위까지
        stk=[]
        while len(arr)>0:
            tmp=arr.pop(0)
            if tmp==o:
                stk.append(operation(stk.pop(), arr.pop(0),o))
            else:
                stk.append(tmp)
        arr=stk #기호 하나 다 없앤 거
    return abs(int(arr[0]))

def solution(expression):
    op=['*','+','-']
    op=list(permutations(op,3))
    result=[]
    for i in op:
        result.append(calculate(expression,i))
    return max(result)