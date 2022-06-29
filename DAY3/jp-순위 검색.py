from itertools import combinations as cmb
from collections import defaultdict

def count_person(li, score):
	""" lower bound 이진탐색 수행 """
	n = len(li)
	
	# x: score미만, o: score이상
	s, e = -1, n-1
	
	while s+1<e:
		mid = (s+e)//2
		if li[mid]>=score:
			e = mid
		else:
			s = mid
	
	if li[e]>=score:
		return n-e
	else:
		return 0

def solution(info, query):

	# defaultdict로 key 유무 검사X - O(n) 단축
	d = defaultdict(list)

	# 모든 query 조합 구하기
	for i in info:
		*li, score = i.split()
		
		for k in range(5):
			cases = cmb([0,1,2,3], k)
			for case in cases:
				cp = list(li)
				for idx in case:
					cp[idx] = '-'
				
				d[''.join(cp)].append(int(score))
	
	# 미리 정렬 (쿼리순회 때 정렬 시 시간초과)
	for k, v in d.items():
		d[k] = sorted(v)
		
	res = []

	# 쿼리 순회 (<=100000)
	for q in query:
		*li, score = q.replace('and ', '').split()
		k = ''.join(list(li))
		if k in d:
			res.append(count_person(d[k], int(score)))
		else:
			res.append(0)
	return res

"""
시간 초과 : query 순회 시 sort 수행 -> O(n^2)

from itertools import combinations as cmb
from collections import defaultdict

def count_person(li, score):
	n = len(li)
	li = sorted(li)
	
	# x: score미만, o: score이상
	if not (score <= li[-1]):
		return 0
	
	if not (li[0] < score):
		return n
	
	s, e = 0, n-1
	
	while s+1<e:
		mid = (s+e)//2
		if li[mid]>=score:
			e = mid
		else:
			s = mid
	return n-e

def solution(info, query):
	
	# 모든 query 조합 구하기
	d = defaultdict(list)
	for i in info:
		*li, score = i.split()
		
		for k in range(5):
			cases = cmb([0,1,2,3], k)
			for case in cases:
				cp = list(li)
				for idx in case:
					cp[idx] = '-'
				
				d[''.join(cp)].append(int(score))

	res = []
	for q in query:
		*li, score = q.replace('and ', '').split()
		k = ''.join(list(li))
		if k in d:
			res.append(count_person(d[''.join(list(li))], int(score)))
		else:
			res.append(0)
	return res

"""