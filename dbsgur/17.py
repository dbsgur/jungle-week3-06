import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline


M, N, H = map(int, input().split())

tomatos = [[[int(x) for x in input().split()]
            for _ in range(N)]for _ in range(H)]


def bfs():
    q = deque()
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if tomatos[k][i][j] == 1:
                    q.append([k, i, j])

    # 상 하 좌 우 위 아래
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and tomatos[nz][nx][ny] == 0:
                tomatos[nz][nx][ny] = tomatos[z][x][y] + 1
                q.append([nz, nx, ny])
    maxD = 0
    for z in range(H):
        for x in range(N):
            if 0 in tomatos[z][x]:
                print(-1)
                return
            maxD = max(maxD, max(tomatos[z][x]))
    print(maxD - 1)


bfs()
