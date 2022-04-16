# 13. 미로 탐색(#2178)
import sys
from collections import deque
sys.stdin = open('input.txt')

[N, M] = list(map(int, sys.stdin.readline().strip().split()))
miro = []

for n in range(N):
    miro.append(sys.stdin.readline().strip())

def bfs(graph, sx, sy, visited):
    distance = []
    for _ in range(N):
        distance.append([1] * M)
    queue = deque([[sx, sy]])
    visited[sx][sy] = True

    while queue:
        [vx, vy] = queue.popleft()
        around = [[vx + 1, vy], [vx, vy + 1], [vx - 1, vy], [vx, vy - 1]] # 현재 위치 주변에 이동가능한 좌표들
        for i in around:
            if i[0] >= N or i[1] >= M:
                continue
            if i[0] < 0 or i[1] < 0:
                continue
            if not visited[i[0]][i[1]] and graph[i[0]][i[1]] == '1': # 아직 방문하지 않았고, 갈 수 있는 좌표면
                distance[i[0]][i[1]] = distance[vx][vy] + 1
                if i[0] == N - 1 and i[1] == M - 1: # 도착지에 도착하면 거리 출력하고 함수 종료
                    print(distance[i[0]][i[1]])
                    return
                queue.append(i)
                visited[i[0]][i[1]] = True
visited = []
for _ in range(N):
    visited.append([False] * M)

bfs(miro, 0, 0,visited)
