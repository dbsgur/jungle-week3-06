import sys
from collections import deque

sys.stdin = open("input.txt")
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph = [[]for _ in range(N+1)]

visited = [False] * (N+1)
distance = [0] * (N+1)
for i in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)

# print(graph)


def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = True
    distance[start] = 0
    results = []
    while q:
        v = q.popleft()
        # if len(q) == 1:
        # count += 1
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                distance[i] = distance[v] + 1
                if distance[i] == K:
                    results.append(i)
    # print(f"results : {results}")
    if len(results) == 0:
        print(-1)
    else:
        results.sort()
        print(*results, sep='\n')


bfs(X)
