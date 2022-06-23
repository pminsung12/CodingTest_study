import re
from collections import deque
from itertools import permutations
from functools import reduce

def calculate(a, b, op):
	""" a, b 에 대해 연산 """
	if op=="+":
		ans = reduce(lambda a,b : a+b, map(int, [a,b]))
	elif op=="-":
		ans = reduce(lambda a,b : a-b, map(int, [a,b]))
	else:
		ans = reduce(lambda a,b : a*b, map(int, [a,b]))
	return ans

def solution(s):
	ans = []
	
	# 연산자 우선순위 순열
	pm = permutations(["*", "-", "+"], 3)
	
	for p in pm:
		
		# 숫자, 연산자 분리 배열
		# s.replace('-', ' - ').replace('+', ' + ').replace('*', ' * ').split()
		q = deque(re.sub("([-+*]{1})", r" \1 ", s).split())
		stack = []
		
		# 연산자 우선순위대로 연산
		for o in p:
			while q:
				curr = q.popleft()
				if curr.isdigit():     # 숫자
					stack.append(curr)
				elif curr == o:        # 우선 연산
					stack.append(str(calculate(stack.pop(), q.popleft(), curr)))
				else:
					stack.append(curr) # 후순위 연산자
					
			q = deque(stack)
			stack = []
			
		ans.append(abs(int(q.popleft())))

	return max(ans)