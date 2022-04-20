import sys
from collections import deque

sys.stdin = open("input.txt")
input = sys.stdin.readline

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    visited[x][y] = True
    while dq:
        sx, sy = dq.popleft()
        for i in range(8):
            nx = sx + dx[i]
            ny = sy + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            if visited[nx][ny] == False and coordinate[nx][ny] == 1:
                dq.append((nx, ny))
                visited[nx][ny] = True


while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    visited = [[False]*w for _ in range(h)]
    coordinate = [[int(x) for x in input().strip().split()] for _ in range(h)]
    count = 0
    # print(f"visited : {visited}")
    # print(f"coordinate : {coordinate}")
    for x in range(h):
        for y in range(w):
            if visited[x][y] == False and coordinate[x][y] == 1:
                bfs(x, y)
                count += 1
    print(count)
