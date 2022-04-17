# 너무어렵네여

import sys
from collections import deque

sys.setrecursionlimit(10**8)

sys.stdin = open("input.txt")

input = sys.stdin.readline

N, M = map(int, input().split())

matrix = [[int(x) for x in input().strip()]for _ in range(N)]

visited = [[False] * N for _ in range(N)]

# !!! 뭔가를 매개변수로 넘겨야할 때는 dfs
# 여기서는 벽 몇개 부쉇는지
# 그러나 매개변수를 안넘겨 줘도 된다면 ?!
# def bfs():
#   dq = deque((x,y,z))
#   while dq :
#     a,b,c = dq.popleft()
#     if a == N-1 and b == M-1 :
#       return visited[a][b][c]
#       ...

# fuck dfs
# results = []
# def dfs(x, y, broke, count):
#     visited[x][y] = True
#     if x == N-1 and y == M-1:
#         results.append(count)
#         return
#     around = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
#     for nx, ny in around:
#         if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False:
#             if broke == 0:
#                 # matrix[x][y] == 1 이면 벽
#                 if matrix[nx][ny] == 1:
#                     visited[nx][ny] = True
#                     dfs(nx, ny, 1, count+1)
#                     visited[nx][ny] = False
#                 else:
#                     visited[nx][ny] = True
#                     dfs(nx, ny, 0, count+1)
#                     visited[nx][ny] = False
#             elif broke == 1:
#                 if matrix[nx][ny] == 0:
#                     visited[nx][ny] = True
#                     dfs(nx, ny, 1, count+1)
#                     visited[nx][ny] = False


# dfs(0, 0, 0, 1)

# if len(results) == 0:
#     print(-1)
# else:
#     print(min(results))
