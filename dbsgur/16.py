import sys
from collections import deque

# sys.stdin = open("input.txt")

input = sys.stdin.readline

n = int(input())

# graph = [[x for x in map(int, input().strip())] for _ in range(n)]
graph = [[int(x) for x in input().strip()] for _ in range(n)]

visited = [[-1]*n for _ in range(n)]

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    dq = deque()
    dq.append((0, 0))
    visited[0][0] = 0
    while dq:
        nowX, nowY = dq.popleft()
        # print("now : ", nowX, nowY)
        for i in range(4):
            nx = nowX + dx[i]
            ny = nowY + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                # print("next : ", nx, ny)
                # print(visited)
                # 0 이면 검은방 -> count ++
                if graph[nx][ny] == 0:
                    dq.append((nx, ny))
                    visited[nx][ny] = visited[nowX][nowY] + 1
                # 아니면 흰방 - > 그냥 진행
                else:
                    dq.appendleft((nx, ny))
                    visited[nx][ny] = visited[nowX][nowY]
                    # 여기 먼저 탐색하라고 appendleft


# print(visited)
bfs()
print(visited[n-1][n-1])
