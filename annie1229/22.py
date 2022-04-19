# 22. 그래프 수정(#1432)
import sys
from heapq import heappush, heappop
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
indegree = [0 for _ in range(N + 1)]
result = [0 for _ in range(N + 1)]

for y in range(1, N + 1):
    line = [0] + list(map(int, sys.stdin.readline().strip()))
    print(line)
    for x in range(1, N + 1):
        if line[x] == 1:
            graph[x].append(y) # 간선 방향 뒤집기 (원래 x -> y, 뒤집은거 y -> x)
            indegree[y] += 1

print(graph)
print(indegree)

def topology_sort():
    q = []
    for i in range(1, N + 1):
        if indegree[i] == 0:
            heappush(q, -i) # 최대 힙에 넣기
    n = N
    while q:
        now = -heappop(q) # 진입 차수 없는 노드 중에 가장 큰 수 pop된다
        result[now] = n # 결과 담는 배열에 새롭게 붙이 숫자 넣어주기(뒤에서부터 큰 수로 배정)
        
        for g in graph[now]:
            indegree[g] -= 1 # 진입 차수 없애주기
            if indegree[g] == 0: # 진입 차수 0인 애들 최대 힙에 넣어주기
                heappush(q, -g)
        n -= 1

topology_sort()

print(result)
if result.count(0) > 1: # 그래프에 사이클이 존재하면 진입차수 0이 안되어서 결과가 0(초기값)인 애들이 있다. 1보다 많을 경우만 체크하는 이유는 0번 인덱스는 항상 0이므로
    print(-1)
    
else:
    print(*result[1:])