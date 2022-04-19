import sys
from collections import deque

sys.setrecursionlimit(10**8)

sys.stdin = open("input.txt")

input = sys.stdin.readline

N, M = map(int, input().split())

matrix = [[int(x) for x in input().strip()]for _ in range(N)]

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
# visited = [[[0] * M for _ in range(N)] for _ in range(2)]

# 상하 좌우
moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def bfs():
    dq = deque()
    dq.append((0, 0, 0))
    while dq:
        x, y, c = dq.popleft()
        if x == N-1 and y == M-1:
            print(visited[x][y][c] + 1)
            return
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            if nx < 0 or ny < 0 or nx >= N or ny >= M or c > 1:
                continue
            if matrix[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[x][y][c] + 1
                dq.append((nx, ny, c))
            elif matrix[nx][ny] == 1 and c == 0:
                visited[nx][ny][c+1] = visited[x][y][c] + 1
                dq.append((nx, ny, c+1))
    print(-1)
    return


bfs()
# def bfs():
#     dq = deque()
#     # x, y, count
#     dq.append((0, 0, 0))
#     visited[0][0] = True
#     flag = False
#     while dq:
#         x, y, c = dq.popleft()
#         print(f"x: {x} y : {y} c: {c}")
#         if c > 1:
#             continue
#         if x == N-1 and y == M-1:
#             print(c)
#             flag = True
#             return
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             print(f"nx : {nx} ny: {ny}")
#             if nx < 0 or ny < 0 or nx >= N or ny >= M or c > 1:
#                 continue
#             if visited[nx][ny] == False:
#                 visited[nx][ny] = True
#                 dq.append((nx, ny, c+1))

#     if not flag:
#         print(-1)


# bfs()

# print(f"N:{N} M :{M}")
