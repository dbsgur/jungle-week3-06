# 4. DFS와 BFS(#1260)
import sys
from collections import deque
sys.stdin = open('input.txt')

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
dfsResult = []
bfsResult = []

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

for n in range(N + 1):
    if graph[n]:
        graph[n].sort()
        
def dfs(graph, start, visited):
    dfsResult.append(start)
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start):
    visited = [False for _ in range(N + 1)]
    q = deque([start])
    visited[start] = True
    bfsResult.append(start)
    
    while q:
        node = q.popleft()
        for i in graph[node]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                bfsResult.append(i)

visited = [False for _ in range(N + 1)]
dfs(graph, V, visited)
bfs(graph, V)
    
print(' '.join(list(map(str, dfsResult))))
print(' '.join(list(map(str, bfsResult))))
