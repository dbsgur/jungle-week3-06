# 7. 트리의 부모 찾기(#11725)
import sys
sys.setrecursionlimit(1000000)
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

graph = [[] for _ in range(N)]
visited = [False] * N
parentDict = {}

for _ in range(N - 1):
    [n1, n2] = list(map(int, sys.stdin.readline().strip().split()))
    graph[n1 - 1].append(n2 - 1)
    graph[n2 - 1].append(n1 - 1)

for g in graph:
    g.sort()

def dfs(idx):
    visited[idx] = True
    for i in graph[idx]:
        if not visited[i]:
            parentDict[i + 1] = idx + 1 # 본인의 부모 노드 번호 담기
            dfs(i)

dfs(0)

for i in range(2, N + 1):
    print(parentDict[i])
