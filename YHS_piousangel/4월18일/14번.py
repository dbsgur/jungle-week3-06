import sys
from collections import deque

sys.stdin = open('sample.txt')
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph = [ [] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)


def bfs(graph, visited, distance, start):
    global correct_list

    q = deque()

    q.append([start, 0])
    visited[start] = 0
   
    while q:
        # print(q)
        now, cnt = q.popleft()
        if cnt == distance and now != start :
            correct_list.append(now)
        
        for i in graph[now]:
            if visited[i] == False:
                visited[i] = True
                q.append([i, cnt+1])

correct_list = []
bfs(graph, visited, K, X)
correct_list.sort()
if len(correct_list) == 0:
    print("-1")
else:
    for i in correct_list:
        print(i)
    
