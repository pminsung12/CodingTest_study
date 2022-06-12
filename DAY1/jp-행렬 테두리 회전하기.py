def solution(rows, columns, queries):

	arr = [[columns*i+j for j in range(1, columns+1)] for i in range(rows)]
	
	def get_minval(r1, c1, r2, c2):
		last = arr[r1-1][c2-1] # (우측모서리끝)

		minval = last

		# 상단
		for c in range(c2-1, c1-1, -1):
			minval = min(minval, arr[r1-1][c-1])
			arr[r1-1][c-1+1] = arr[r1-1][c-1]

		# 좌측
		for r in range(r1+1, r2+1):
			minval = min(minval, arr[r-1][c1-1])
			arr[r-1-1][c1-1] = arr[r-1][c1-1]

		# 하단
		for c in range(c1+1, c2+1):
			minval = min(minval, arr[r2-1][c-1])
			arr[r2-1][c-1-1] = arr[r2-1][c-1]

		# 우측
		for r in range(r2-1, r1-1, -1):
			minval = min(minval, arr[r-1][c2-1])
			arr[r-1+1][c2-1] = arr[r-1][c2-1]

		# 우상단 아랫값 갱신
		arr[r1-1+1][c2-1] = last

		return minval
		
	res = []
	for loc in queries:
		res.append(get_minval(*loc))
	return res