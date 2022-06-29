from collections import defaultdict
def solution(clothes):
    d = defaultdict(int)
    for _, category in clothes:
        d[category] +=1
        
    answer = 1
    for category in d:   
        answer *= (d[category] + 1) # "안입음" 추가
    
	# "모두 안입음" 제외
    return answer - 1

# 숏코드 : Counter + reduce
# reduce(func, iterable, initializer) : initializer 을 첫번째 값으로 시작
from collections import Counter
from functools import reduce
def solution(clothes):
    counter = Counter([category for _, category in clothes])
    answer = reduce(lambda x, y: x*(y+1), counter.values(), 1) - 1
    return answer


"""
# 시간초과 - 재귀 완전탐색
# 복잡도는?
from collections import defaultdict

def solution(clothes):

	d = defaultdict(list)
	visited = defaultdict(list)
	
	for cloth, category in clothes:
		d[category].append(cloth)
		visited[category].append(0)
		
	# "없음" 추가, 정수로 변환(idx로 사용)
	for k in d:
		d[k].append('-')
		visited[category].append(0)
		d[k] = list(range(len(d[k])))

	keys = list(d.keys())
	n = len(keys)
	cnt = 0

	# n번 재귀 실행
	def recur(curr, res):
		nonlocal cnt, d, visited
		if curr>=n:
			cnt+=1
			return
			
		category = keys[curr]
		
		for cloth in d[category]:
			visited[category][cloth] = 1
			recur(curr+1, res+[cloth])
			visited[category][cloth] = 0
		
	recur(0, [])

	# 개수 출력 ("모두 없음" 제외)
	return cnt-1
"""