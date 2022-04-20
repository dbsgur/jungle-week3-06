# 이게 18 왜 틀림?
import sys
from collections import deque

sys.stdin = open("input.txt")
input = sys.stdin.readline

N, M = map(int, input().split())

r, c, d = map(int, input().split())

home = [[int(x) for x in input().strip().split()] for _ in range(N)]

visited = [[False] * M for _ in range(N)]

# print(home)
# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    global d
    dq = deque()
    # home[r][c] = 1
    visited[r][c] = True
    dq.append((r, c))
    count = 1
    while dq:
        sx, sy = dq.popleft()
        check = False
        for _ in range(4):
            d += 3
            nx = sx + dx[d % 4]
            ny = sy + dy[d % 4]
            if nx < 0 or ny < 0 or nx >= N or nx >= M:
                continue
            if home[nx][ny] == 0 and visited[nx][ny] == False:
                visited[nx][ny] = True
                # home[nx][ny] = 1
                dq.append((nx, ny))
                count += 1
                check = True
                break

        if check == False:
            nx = sx - dx[(d) % 4]
            ny = sy - dy[(d) % 4]
            if nx < 0 or ny < 0 or nx >= N or nx >= M:
                print(count)
                return
            if home[nx][ny] == 1:
                print(count)
                return
            visited[nx][ny] = True
            dq.append((nx, ny))


bfs()
