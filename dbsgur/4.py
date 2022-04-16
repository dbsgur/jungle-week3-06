import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline


def dfs(n):
    print(n, end=' ')
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i)


def bfs(n):
    visited[n] = True
    queue = deque([n])
    while queue:
        v = queue.popleft()
        print(f"{v}", end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for lines in graph:
    lines.sort()

visited = [False]*(N+1)

dfs(V)

visited = [False] * (N+1)

print()
bfs(V)
