# 16. 미로 만들기(#2665)
import sys
from collections import deque

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
rooms = []

def bfs(graph, sx, sy):
    changes = [] # 방 색상 변화 정보 담을 배열
    for _ in range(N):
        changes.append([sys.maxsize] * N) # 탐색하지 않은 위치는 변화 값 무한대로 설정
    queue = deque([[sx, sy]])
    changes[0][0] = 0 # 시작 위치 변화 0으로
    while queue:
        [vx, vy] = queue.popleft()
        around = [[vx + 1, vy], [vx, vy + 1], [vx - 1, vy], [vx, vy - 1]]
        for i in around:
            if i[0] >= N or i[1] >= N:
                continue
            if i[0] < 0 or i[1] < 0:
                continue
            if changes[i[0]][i[1]] > changes[vx][vy]: # 이동할 칸의 변화값이 현재칸 변화값보다 크면
                if graph[i[0]][i[1]] != 1: # 검은 방이었으면
                    changes[i[0]][i[1]] = changes[vx][vy] + 1 # 변화 값 증가
                else: # 흰 방이었으면
                    changes[i[0]][i[1]] = changes[vx][vy] # 변화 값 그대로
                queue.append(i)
    return changes[N - 1][N - 1]

for n in range(N):
    line = list(map(int, sys.stdin.readline().strip()))
    rooms.append(line)

print(bfs(rooms, 0, 0))