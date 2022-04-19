# 9. 아침 산책(#21606) 73점..
import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

places = list(map(int,sys.stdin.readline().strip()))
inside = []
outside = []
graph = [[] for _ in range(N + 1)]

for idx, place in enumerate(places):
    if place:
        inside.append(idx + 1)
    else:
        outside.append(idx + 1)

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start, visited):
    global route

    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            if places[i - 1] == 0:
                print('산책 중', start)
                dfs(i, visited)
            else:
                print('산책 종료', i)
                route += 1
                         
route = 0
for i in inside:
    visited = [False for _ in range(N + 1)]
    print('산책 시작', i)
    dfs(i, visited)
    print('-------')
print(route)
