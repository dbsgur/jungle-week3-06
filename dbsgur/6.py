import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

vertex = int(input())
edges = int(input())

visited = [False]*(vertex+1)

graph = [[]for _ in range(vertex+1)]

for _ in range(edges):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(f"graph : {graph}")


def bfs():
    count = 0
    dq = deque()
    dq.append(1)
    visited[1] = True
    while dq:
        now = dq.popleft()
        for i in graph[now]:
            if visited[i] == False:
                dq.append(i)
                visited[i] = True
                print(f"i : {i}")
                count += 1

    return count


print(bfs())
print(visited)

# 옛날에 dfs로 푼 코드
# dfs가 미세하지만 더 빠르다.
# 이유는 모르겠다.

# import sys

# input = sys.stdin.readline

# N = int(input())
# M = int(input())

# graph = [[] * N for _ in range(N+1)]

# for _ in range(M):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# cnt = 0
# visited = [0] * (N+1)


# def dfs(start):
#     global cnt
#     visited[start] = 1
#     for i in graph[start]:
#         if visited[i] == 0:
#             dfs(i)
#             cnt += 1


# dfs(1)
# print(cnt)
