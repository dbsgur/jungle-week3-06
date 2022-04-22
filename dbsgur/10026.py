import sys
import copy
from collections import deque
sys.stdin = open('input.txt')

N = int(input())

picture = [[x for x in input().strip()] for _ in range(N)]

visited = [[False]*N for _ in range(N)]

# 상하 좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    color = picture[x][y]
    while dq:
        sx, sy = dq.popleft()
        for i in range(4):
            nx = sx + dx[i]
            ny = sy + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if visited[nx][ny] == False and picture[nx][ny] == color:
                dq.append((nx, ny))
                visited[nx][ny] = True


def bfsS(x, y):
    dq = deque()
    dq.append((x, y))
    color = picture[x][y]
    while dq:
        sx, sy = dq.popleft()
        for i in range(4):
            nx = sx + dx[i]
            ny = sy + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if color == "R" or color == "G":
                if visited[nx][ny] == False and (picture[nx][ny] == "R" or picture[nx][ny] == "G"):
                    dq.append((nx, ny))
                    visited[nx][ny] = True
                    continue
            elif visited[nx][ny] == False and picture[nx][ny] == color:
                # print(f"color : {color}")
                dq.append((nx, ny))
                visited[nx][ny] = True


count = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            bfs(i, j)
            count += 1
visited = [[False]*N for _ in range(N)]
countT = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            bfsS(i, j)
            countT += 1

print(count)
print(countT)
