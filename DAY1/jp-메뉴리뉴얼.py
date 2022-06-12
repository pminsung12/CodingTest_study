from itertools import combinations
from collections import Counter

def solution(orders, course):
	answer = []
	for k in course:
		combs = [''.join(sorted(c)) for menus in orders for c in combinations(menus, k)]		
		most = Counter(combs).most_common() # [(menus, cnt).. ] 내림차순
		answer += [menus for menus, cnt in most if cnt>1 and cnt == most[0][1]]
	return sorted(answer)