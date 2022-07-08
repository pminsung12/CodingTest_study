import heapq

def dijkstra(dist, graph):
    heap=[]
    heapq.heappush(heap,[0,1]) #[거리, 노드] , 앞의 원소인 거리가 최소인 값으로 힙이 정렬됨.
    while heap:
        cost, node=heapq.heappop(heap) #1에서 node로 가기 위한 최소 cost를 pop 해줌.
        for c,n in graph[node]:#node 에서 갈 수 있는 다른 node들 돌리면서 최솟값에 cost + 해줌.
            if cost+c<dist[n]:#최솟값 경신
                dist[n]=cost+c
                heapq.heappush(heap,[cost+c,n])
    

def solution(N, road, K):
    answer = 0
    INF=float('inf')
    dist=[INF]*(N+1) #최솟값 저장 배열
    dist[1]=0 #자기 자신이니까 거리 0
    graph=[[] for _ in range(N+1)]
    
    for i in road:
        graph[i[0]].append((i[2],i[1]))
        graph[i[1]].append((i[2],i[0]))
    
    dijkstra(dist,graph)

    return len([i for i in dist if i<=K])