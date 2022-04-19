import sys
from collections import deque

sys.stdin = open("input.txt")
input = sys.stdin.readline

T = int(input())

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    visited[x][y] = True
    dq = deque()
    dq.append((x, y))
    while dq:
        nowX, nowY = dq.popleft()
        for i in range(4):
            nx = nowX + dx[i]
            ny = nowY + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if cabbage[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                dq.append((nx, ny))


for _ in range(T):
    M, N, K = map(int, input().split())

    cabbage = [[0]*M for _ in range(N)]

    visited = [[False]*M for _ in range(N)]

    for i in range(K):
        x, y = map(int, input().split())
        cabbage[y][x] = 1

    count = 0

    for i in range(N):
        for j in range(M):
            if cabbage[i][j] == 1 and visited[i][j] == False:
                bfs(i, j)
                count += 1

    print(count)
