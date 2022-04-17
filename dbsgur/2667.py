import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())

matrix = [[int(x) for x in input().strip()]for _ in range(N)]

count = 0

visited = [[False]*N for _ in range(N)]

# print(visited)

peoples = []


def bfs(startX, startY):
    dq = deque()
    dq.append([startX, startY])
    visited[startX][startY] = True
    count = 1
    while dq:
        nowX, nowY = dq.popleft()
        around = [[nowX-1, nowY], [nowX+1, nowY],
                  [nowX, nowY-1], [nowX, nowY+1]]
        for x, y in around:
            if 0 <= x < N and 0 <= y < N and visited[x][y] == False and matrix[x][y] == 1:
                visited[x][y] = True
                dq.append([x, y])
                count += 1
    peoples.append(count)


# 매트릭스 처음부터 1인애들 찾아서 bfs 실행
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1 and visited[i][j] == False:
            bfs(i, j)
            count += 1
# count

# print(matrix)

if count == 0:
    print(0)
else:
    print(count)
    peoples.sort()
    print(*peoples, sep='\n')
