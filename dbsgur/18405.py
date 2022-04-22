import sys
from collections import deque
import heapq
sys.stdin = open("input.txt")
input = sys.stdin.readline

N, K = map(int, input().split())

virus = [[int(x) for x in input().strip().split()] for _ in range(N)]

s, xx, yy = map(int, input().split())

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move():
    heap = []
    for x in range(N):
        for y in range(N):
            if virus[x][y] > 0:
                heapq.heappush(heap, (virus[x][y], (x, y)))
                # dq.append((x, y, virus[x][y]))
                # num += 1
    # while dq:
    while heap:
        # sx, sy, n = dq.popleft()
        n, (sx, sy) = heapq.heappop(heap)

        for i in range(4):
            nx = sx + dx[i]
            ny = sy + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if virus[nx][ny] == 0:
                virus[nx][ny] = n
    if virus[xx-1][yy-1] > 0:
        print(virus[xx-1][yy-1])
        sys.exit(0)


for i in range(s):
    move()

# print(virus[xx-1][yy-1])
if s == 0:
    print(virus[xx-1][yy-1])
    sys.exit(0)
print(0)
