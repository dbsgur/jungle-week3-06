import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

citys = [[int(x) for x in input().strip().split()] for _ in range(N)]


# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, h):
    dq = deque()
    dq.append((x, y))
    visited[x][y] = True
    while dq:
        sx, sy = dq.popleft()
        for i in range(4):
            nx = sx+dx[i]
            ny = sy+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] == False and citys[nx][ny] > h:
                dq.append((nx, ny))
                visited[nx][ny] = True


maxH = 0
minH = 101
for city in citys:
    maxH = max(*city, maxH)
    minH = min(*city, minH)
# print(f"maxH : {maxH}")
maxC = 0
for h in range(minH-1, maxH):
    count = 0
    visited = [[False] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if visited[x][y] == False and citys[x][y] > h:
                bfs(x, y, h)
                count += 1
    maxC = max(count, maxC)

print(maxC)
