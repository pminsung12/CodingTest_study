#Brute force, 시뮬레이션
dx=[1,0,-1,0]#우 하 좌 상
dy=[0,-1,0,1]
def solution(grid):
    answer = []
    global visited, n, m
    n=len(grid)
    m=len(grid[0])
    visited=[[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]
    for nx in range(n):
        for ny in range(m):
            for d in range(4):
                if not visited[nx][ny][d]:
                    res=simul(nx,ny,d,grid)
                    if res!=0:
                        answer.append(res)
    answer.sort()
    return answer

def simul(x,y,d,grid):
    global visited,n,m
    nx,ny,nd=x,y,d
    cnt=0
    visited[x][y][d]=True
    while True:
        nx=(nx+dx[nd])%n #격자뚫는 거를 %n으로 계산, 한칸씩 밖에 안움직이니까
        ny=(ny+dy[nd])%m
        cnt+=1
        
        if grid[nx][ny]=='R':#하 좌
            nd=(nd+1)%4
        elif grid[nx][ny]=='L':#하 우
            nd=(nd-1)%4
        #S면 방향 그대로니까
        if visited[nx][ny][nd]:
            if(nx,ny,nd)==(x,y,d):
                return cnt
            else:
                return 0
        visited[nx][ny][nd]=True
            
        