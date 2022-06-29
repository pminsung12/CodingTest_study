def solution(n, arr, thr):
	# 노드별 (연결노드, 거리) 저장
	g = [[float("inf") for _ in range(n+1)] for _ in range(n+1)]

	for a in arr:
		g[a[0]][a[1]] = min(g[a[0]][a[1]], a[2])
		g[a[1]][a[0]] = min(g[a[0]][a[1]], a[2])
		
	# 자신 -> 자신 : 0
	for i in range(1, n+1):
		g[i][i] = 0
	
    # 플로이드워셜
	for k in range(1, n+1):
		for i in range(1, n+1):
			for j in range(1, n+1):
				g[i][j] =  min(g[i][j], g[i][k]+g[k][j])
			
	return sum([1 for d in g[1] if d<=thr])