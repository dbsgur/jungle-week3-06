# 21. 장난감조립(#2637)
import sys
from collections import deque
sys.stdin = open('input.txt')

N = int(sys.stdin.readline()) # 총 부품 수(=완제품의 번호)
M = int(sys.stdin.readline()) # 부품들 관계의 수
graph = [[] for _ in range(N + 1)] # 부품들 순서 관계 담을 그래프
indegree = [0 for _ in range(N + 1)] # 진입차수 담을 배열
assemble = [[0 for _ in range(N + 1)] for _ in range(N + 1)] # 필요한 총 재료 담을 배열

for _ in range(M):
    X, Y, K = map(int, sys.stdin.readline().split())
    graph[Y].append([X, K]) # 선 관계에 있는 재료들(Y)에 후 관계에 있는 [조립부품, 부품 갯수]추가
    indegree[X] += 1 # 진입차수 증가
    
def topology_sort():
    q = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0: # 진입차수가 0인노드들 큐에 추가
            q.append(i)

    while q:
        now = q.popleft()
        for g, need in graph[now]:
            if assemble[now].count(0) == N + 1: # now 재료를 만들기 위한 조립재료들이 필요 없다면
                assemble[g][now] += need # 그냥 필요한 개수만큼 추가
            else: # now 재료를 만들기 위해 조립이 필요하다면
                for i in range(1, N+1):
                    assemble[g][i] += assemble[now][i] * need # 조립에 사용된 각 부품 * 필요한 갯수 해서 더하기

            indegree[g] -= 1 # 진입차수 감소
            if indegree[g] == 0:
                q.append(g) # 새롭게 진입차수 0된 애들 큐에 담기

    for idx, cnt in enumerate(assemble[N]):
        if cnt > 0:
            print(f'{idx} {cnt}')

topology_sort()