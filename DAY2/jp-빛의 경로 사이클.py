def solution(grid):
    answer = []
    n, m = len(grid), len(grid[0])

    # r, c 에서 d방향으로 나갔는지 여부
    visited = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]

    # rotate 함수 사용 고려해서 순서 배정 (idx 증가: R, idx감소: L)
    directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]  # D, L, U, R

    def move(r, c, d):
        nonlocal directions, n, m
        dx, dy = directions[d]
        return (r + dx) % n, (c + dy) % m

    def rotate(d, node):
        """directions 배열 내 방향 순서도 중요"""
        if node == "R":
            d = (d + 1) % 4
        elif node == "L":
            d = (d - 1) % 4
        return d

    for r in range(n):
        for c in range(m):
            for d in range(4):
                # 방향, 위치 첫 탐색 시 cycle 계산
                if not visited[r][c][d]:
                    cx, cy, cd = r, c, d
                    cnt = 0
                    while not visited[cx][cy][cd]:
                        visited[cx][cy][cd] = True
                        cnt += 1
                        cx, cy = move(cx, cy, cd)  # 다음 위치
                        cd = rotate(cd, grid[cx][cy])  # 다음 위치에서 나가는 방향
                    answer.append(cnt)
    return sorted(answer)
