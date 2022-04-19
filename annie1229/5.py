# 5. 연결 요소의 개수(#11724)
import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input.txt')

V, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [True] + [False for _ in range(V)]

def dfs(start):
    global visited
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

count = 1

for idx, v in enumerate(visited):
    if not v:
        dfs(idx)
        if visited.count(False):
            count += 1
        else:
            print(count)
            break
