import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline


M, N = map(int, input().split())

tomatos = [[int(x) for x in input().split()]for _ in range(N)]


def bfs():

    q = deque()
    for i in range(N):
        for j in range(M):
            if tomatos[i][j] == 1:
                q.append([i, j])

    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and tomatos[nx][ny] == 0:
                tomatos[nx][ny] = tomatos[x][y] + 1
                q.append([nx, ny])
            # if nx < 0 or nx >= N or ny < 0 or ny >= M:
            #     continue
            # if tomatos[nx][ny] == -1:
            #     continue
            # elif tomatos[nx][ny] == 0:
            #     tomatos[nx][ny] = tomatos[x][y] + 1
            #     q.append((nx, ny))
            # elif tomatos[nx][ny] > 0:
            #     tomatos[nx][ny] = min(tomatos[nx][ny], tomatos[x][y] + 1)
    maxD = 0
    for i in range(N):
        if 0 in tomatos[i]:
            print(-1)
            return
        maxD = max(maxD, max(tomatos[i]))
    print(maxD-1)


bfs()
