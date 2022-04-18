import sys 
from collections import deque
sys.stdin = open('sample.txt')

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [ [] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):

    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(n):
    q = deque([n])

    while q:
        temp = q.popleft()

        for x in graph[temp]:
            if visited[x] == False:
                visited[x] = True
                q.append(x)

for i in range(1, n+1):
    if visited[i] == False:
        bfs(i)
        answer += 1

print(answer)

