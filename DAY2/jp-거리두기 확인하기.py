from collections import deque

def bfs(i,j,p):
	"""
	사람(P)부터 다음 사람(P)을 찾을 때까지 BFS 수행
	거리두기 미충족 시 False 반환
	"""
	
	# P마다 방문 초기화 (자신 기준으로 새로 검사할 수 있도록)
	visited = [[0 for _ in range(5)] for _ in range(5)]
	visited[i][j] = 1
	
	dr = [1,-1,0,0]
	dc = [0,0,1,-1]
	
	# 출발위치 (행, 열, 출발지로부터 맨해튼거리)
	q = deque([(i, j, 0)])
	
	# BFS 수행
	while q:
		r, c, d = q.popleft()
		for i in range(4):
			nr, nc = r+dr[i], c+dc[i]

			# 배열 내 좌표, 미방문, 칸막이 아닐 때
			if 0<=nr<5 and 0<=nc<5 and visited[nr][nc] ==0 and p[nr][nc]!="X":
				
				# 사람일 때
				if p[nr][nc] == "P": # P

					# 맨해튼거리가 2 이내 : False
					if d+1<=2:
						return 0
					else:
						return 1
				
				# 테이블일 때 : enqueue, 방문처리
				else:                
					q.append((nr, nc, d+1))
					visited[nr][nc] = 1					
	return 1

def solution(places):

	# 정답배열
	result = []

	# map 순회
	for p in places:

		# 각 map의 거리두기 충족여부
		flag = True

		# map 내 모든 사람(P) 위치 저장
		locs = [(i, j) for i in range(5) for j in range(5) if p[i][j] == "P"]
		
		# 사람(P) 순회하며 BFS
		for i,j in locs:

			# 미충족 시 break, flag 처리
			if not bfs(i,j,p):
				flag = False
				break
		
		# 해당 map의 거리두기 상태 저장
		if not flag:
			result.append(0)
		else:
			result.append(1)
			
	return result