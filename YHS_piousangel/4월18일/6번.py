import sys
from collections import deque

sys.stdin = open('sample.txt')
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [ [] for _ in range(N+1)]
visited = [False] * (N+1)


for i in range(M) :

    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)


cnt = 0
def bfs(graph, start_num) :
    global cnt
    q = deque()
    q.append(start_num)
    visited[start_num] = True

    while q :

        now = q.popleft()

        for node in graph[now]:
            if visited[node] != True:
                visited[node] = True
                q.append(node)
                cnt += 1
                
bfs(graph, 1)
print(cnt)