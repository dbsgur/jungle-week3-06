import sys
from collections import deque

sys.stdin = open("input.txt")

input = sys.stdin.readline

N, M = map(int, input().split())

matrix = [[int(x) for x in input().strip()] for _ in range(N)]

visited = [[False]*M for _ in range(N)]

# print(f"visited : {visited[0]}")
# print(f"matrix : {matrix[1][0]}")
# print(f"matrix : {matrix}")


def bfs(x, y):
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if matrix[nx][ny] == 0:
                continue

            if matrix[nx][ny] == 1:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append((nx, ny))
    return matrix[N-1][M-1]


print(bfs(0, 0))
