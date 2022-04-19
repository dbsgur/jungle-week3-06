# 3. 최소 스패닝 트리(#1197)
import sys
import heapq
sys.stdin = open('1.in')

V, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    A, B, W = map(int, sys.stdin.readline().split())
    graph[A].append([W, B])
    graph[B].append([W, A])

def prim_mst(start):
    visited = [False for _ in range(V + 1)]
    weight = [sys.maxsize for _ in range(V + 1)] # 모든 정점 초기값 무한대로 설정
    weight[start] = 0 # 시작 정점 0으로 설정
    pq = [(0, start)] # 우선순위 큐(최소힙)
    answer = 0

    while pq:
        cur = heapq.heappop(pq) # 최소힙에서 정점 pop (가장 간선의 가중치가 작은 정점이 나옴)
        curNode = cur[1] # 정점 값
        curDis = cur[0] # 간선 가중치

        if not visited[curNode]: # 방문 안했으면
            visited[curNode] = True # 방문 체크
            answer += curDis # 결과값에 더해주기

            for i in graph[curNode]: # 연결되어있는 정점들 확인
                nextNode = i[1]
                nextDis = i[0]
    
                if not visited[nextNode]: # 아직 방문 안한 정점 있으면 최소힙에 넣기 (이 부분 없이 다 최소힙에 넣어도 통과 되기는 하지만 시간이 훨씬 오래 걸림)
                    heapq.heappush(pq, (nextDis, nextNode))    
    
    print(answer)

prim_mst(1)
