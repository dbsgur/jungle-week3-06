import sys
from collections import deque

sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())


def bfs(graph, visited, idx):

    q = deque()

    q.append(graph[idx])
    visited[idx] = 1
    flag = False
    while q:
        
        temp_arr = q.popleft()
        # print(temp_arr)

        for node in temp_arr :
            if visited[node] == 0 :
                if flag:
                    visited[node] = 2
                    q.append(graph[node])
                    flag = False
                    break
                else:
                    visited[node] == 1
                    q.append(graph[node])
                    flag = True
                    break
            else:
                if visited[node] == 1 or visited[node] == 2:
                    return False 
    return True

for i in range(n):
    v, e = map(int, input().split())
    graph = [ [] for _ in range(v+1)]
    visited = [0] * (v+1)
    for i in range(e):
        a, b = map(int, input().split())

        graph[a].append(b)
     
    
    result = bfs(graph, visited, 1)
    print(visited)
    if result :
        print("YES")
    else:
        print("NO")
    