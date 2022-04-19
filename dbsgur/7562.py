import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

T = int(input())

# 말 이동 방향
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(sx, sy):
    dq = deque()
    dq.append((sx, sy, 0))
    visited[sx][sy] = True
    flag = False
    while dq:
        x, y, count = dq.popleft()
        if flag:
            return
        if x == endX and y == endY:
            print(count)
            flag = True
            return
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= length or ny < 0 or ny >= length:
                continue
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                dq.append((nx, ny, count+1))


for _ in range(T):
    length = int(input())
    startX, startY = map(int, input().split())
    endX, endY = map(int, input().split())
    visited = [[False]*length for _ in range(length)]
    bfs(startX, startY)
    # print(f"length : {length}")
    # print(f"startX : {startX} , startY : {startY}")
    # print(f"endX : {endX}, endY : {endY}")
