import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N, M = map(int, input().split())

edges = [[]for _ in range(N+1)]

visited = [False]*(N+1)

for _ in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)


def dfs(n):
    if visited[n] == True:
        return
    visited[n] = True
    for v in edges[n]:
        if visited[v] == False:
            dfs(v)


count = 0
for i in range(1, N+1):
    if visited[i] == False:
        dfs(i)
        count += 1


print(count)
# print(edges)
