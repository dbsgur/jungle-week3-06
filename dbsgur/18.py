import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

R, C = map(int, input().split())

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

forest = [[x for x in input().strip()]for _ in range(R)]

visited = [[0]*C for _ in range(R)]


def waterBfs():
    waterQ = deque()
    flag = False
    for i in range(R):
        for j in range(C):
            if forest[i][j] == "*":
                waterQ.append((i, j))
    while waterQ:
        x, y = waterQ.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if forest[nx][ny] != "D" and forest[nx][ny] != "X" and forest[nx][ny] != "*" and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                waterQ.append((nx, ny))
    for i in range(R):
        for j in range(C):
            if forest[i][j] == "S":
                waterQ.append((i, j, 0))
                break
    while waterQ:
        x, y, d = waterQ.popleft()
        if forest[x][y] == "D":
            flag = True
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if visited[nx][ny] > d+1 or visited[nx][ny] == 0:
                if forest[nx][ny] == "D" or forest[nx][ny] == ".":
                    waterQ.append((nx, ny, d+1))

    if not flag:
        print("KAKTUS")
    else:
        print(f"{d}")


waterBfs()


# 정답 코드
# def bfs():
#     dq = deque()
#     flag = False
#     for i in range(R):
#         for j in range(C):
#             # water
#             if forest[i][j] == "*":
#                 dq.append((i, j))
#             # goal
#             elif forest[i][j] == "D":
#                 goalX = i
#                 goalY = j
#             # mole
#             elif forest[i][j] == "S":
#                 dq.appendleft((i, j))
#     while dq:
#         x, y = dq.popleft()
#         if flag:
#             break
#         around = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
#         for nx, ny in around:
#             if nx < 0 or nx >= R or ny < 0 or ny >= C:
#                 continue
#             if forest[x][y] == "S":
#                 if forest[nx][ny] == ".":
#                     forest[nx][ny] = "S"
#                     visited[nx][ny] = visited[x][y] + 1
#                     dq.append((nx, ny))
#                 elif forest[nx][ny] == "D":
#                     flag = True
#                     visited[nx][ny] = visited[x][y] + 1
#                     break
#             elif forest[x][y] == "*":
#                 if forest[nx][ny] == "." or forest[nx][ny] == "S":
#                     forest[nx][ny] = "*"
#                     dq.append((nx, ny))
#     if flag:
#         return visited[goalX][goalY]
#     else:
#         return "KAKTUS"


# print(bfs())

# feat, 도영
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]


# def bfs_flood():
#     while queue:
#         time, row, col = queue.popleft()
#         for dir in range(4):
#             n_row, n_col = row + dx[dir], col + dy[dir]
#             if 0 <= n_row < R and 0 <= n_col < C:
#                 if (_map[n_row][n_col] == '.' and _map[n_row][n_col] != '*') or _map[n_row][n_col] == 'S':
#                     _map[n_row][n_col] = time + 1
#                     queue.append((time + 1, n_row, n_col))


# def bfs_gosum():
#     global answer
#     while queue:
#         time, row, col = queue.popleft()

#         for dir in range(4):
#             n_row, n_col = row + dx[dir], col + dy[dir]
#             if 0 <= n_row < R and 0 <= n_col < C:
#                 if _map[n_row][n_col] == 'D':
#                     answer = time + 1
#                     return
#                 elif _map[n_row][n_col] == '.':
#                     queue.append((time + 1, n_row, n_col))
#                 elif _map[n_row][n_col] != 'S' and _map[n_row][n_col] != 'X' and _map[n_row][n_col] > time + 1:
#                     queue.append((time + 1, n_row, n_col))


# R, C = map(int, sys.stdin.readline().split())
# _map = [list(sys.stdin.readline().strip()) for _ in range(R)]
# answer = 0
# flag = True
# queue = deque()

# for i in range(R):
#     for j in range(C):
#         if _map[i][j] == '*':
#             queue.append(('*', i, j))

# for i in range(R):
#     for j in range(C):
#         if _map[i][j] == 'S':
#             _map[i][j] = 0
#             queue.append((0, i, j))


# while queue and flag:
#     what, row, col = queue.popleft()
#     for dir in range(4):
#         n_row, n_col = row + dx[dir], col + dy[dir]
#         if 0 <= n_row < R and 0 <= n_col < C:
#             if what == '*':
#                 if _map[n_row][n_col] not in ['*', 'X', 'D']:
#                     _map[n_row][n_col] = '*'
#                     queue.append(('*', n_row, n_col))
#             else:
#                 if _map[n_row][n_col] == '.':
#                     _map[n_row][n_col] = what + 1
#                     queue.append((what + 1, n_row, n_col))
#                 elif _map[n_row][n_col] == 'D':
#                     answer = what + 1
#                     flag = False
#                     break

# print('KAKTUS' if flag else answer)
