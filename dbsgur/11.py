import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

N, M = map(int, input().split())

glaciers = [[int(x) for x in input().strip().split()] for _ in range(N)]

# 상하 좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    visited[x][y] = True
    dq = deque()
    dq.append((x, y))

    while dq:
        count = 0
        a, b = dq.popleft()
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            if 0 > nx or nx >= N or ny < 0 or ny >= M:
                continue
            if glaciers[nx][ny] == 0 and visited[nx][ny] == False:
                count += 1
            elif glaciers[nx][ny] > 0 and visited[nx][ny] == False:
                visited[nx][ny] = True
                dq.append((nx, ny))
        glaciers[a][b] = max(0, glaciers[a][b] - count)


years = 0
while True:
    lump = 0
    visited = [[False]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if glaciers[i][j] != 0 and visited[i][j] == False:
                bfs(i, j)
                lump += 1
    years += 1
    if lump >= 2:
        print(years-1)
        break
    elif lump == 0:
        print(0)
        break
