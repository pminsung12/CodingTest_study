from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])

    def bfs(i, j):
        nonlocal n, m
        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]

        # 방문여부
        visited = [[0 for _ in range(m)] for _ in range(n)]
        visited[i][j] = 1

        q = deque([(i, j, 1)])  # 시작점: 거리 1

        dist = []
        while q:
            r, c, cost = q.popleft()

            # 적진영 도착
            if (r, c) == (n - 1, m - 1):
                dist.append(cost)

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                # 진행: 미방문, 벽X
                if (
                    0 <= nr < n
                    and 0 <= nc < m
                    and visited[nr][nc] == 0
                    and maps[nr][nc] == 1
                ):
                    q.append((nr, nc, cost + 1))
                    visited[nr][nc] = 1

        # 적진영 미도착
        if visited[n - 1][m - 1] == 0:
            return -1
        else:
            return min(dist)

    return bfs(0, 0)
