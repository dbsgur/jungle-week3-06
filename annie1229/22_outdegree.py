# 22. 그래프 수정(#1432)
import sys
from heapq import heappush, heappop
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
outdegree = [0 for _ in range(N + 1)]
result = [0 for _ in range(N + 1)]

for y in range(1, N + 1):
    line = [0] + list(map(int, sys.stdin.readline().strip()))
    print(line)
    for x in range(1, N + 1):
        if line[x] == 1:
            graph[y].append(x)
            outdegree[y] += 1 # 진출 차수 카운트

print(graph)
print(outdegree)

def reverse_topology_sort():
    q = []
    for i in range(1, N + 1):
        if outdegree[i] == 0:
            heappush(q, -i) # 최대 힙에 넣기
    n = N
    while q:
        now = -heappop(q) # 진출 차수 없는 노드 중에 번호 가장 큰거 pop된다
        result[now] = n # 결과 담는 배열에 새롭게 붙이 숫자 넣어주기(뒤에서부터 큰 수로 배정)
        
        for idx, g in enumerate(graph):
            if now in g:
                outdegree[idx] -= 1 # 진출 차수 없애주기
                if outdegree[idx] == 0: # 진출 차수 0인 애들 최대 힙에 넣기
                    heappush(q, -idx)
        n -= 1

reverse_topology_sort()

print(result)
if result.count(0) > 1: # 그래프에 사이클이 존재하면 진입차수 0이 안되어서 결과가 0(초기값)인 애들이 있다. 1보다 많을 경우만 체크하는 이유는 0번 인덱스는 항상 0이므로
    print(-1)
    
else:
    print(*result[1:])