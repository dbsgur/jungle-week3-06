from collections import deque

def dfs(n):
    print(n, end= ' ')
    visited[n] = True  
    for x in graph[n]:
        if visited[x] != True:
            #visited[x] = True
            dfs(x)
           
def bfs(n):
    q = deque([n]) 
    visited[n] = True
    #q.append([n])
    
    while q:
        temp = q.popleft()
        print(temp, end= ' ')
        for x in graph[temp]:
            if visited[x] != True :
                visited[x] = True
                q.append(x)
                   
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()
    
dfs(v)
visited = [False] * (n+1)
print()
bfs(v)