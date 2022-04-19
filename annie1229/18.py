# 18. 탈출(#3055)
import sys
from collections import deque
sys.stdin = open('input.txt')

R, C = map(int, sys.stdin.readline().split())
mountain_map = [] # 지도 정보 담을 배열
waters = [] # 물 초기 위치 담을 배열
s = [] # 시작 좌표 담을 변수
visited = [] # 방문 체크

for r in range(R):
    visited.append([False for _ in range(C)])
for r in range(R):
    line = list(sys.stdin.readline().strip())
    mountain_map.append(line)
    for idx, l in enumerate(line):
        if l == '*':
            waters.append([r, idx]) # 물 위치 담기
            visited[r][idx] = True  # 물이 있는 곳은 고슴도치가 못가니까 방문 체크 True로 해줌
        if l == 'S':
            s = [r, idx]
            visited[r][idx] = True # 시작위치 방문 체크 True로 해줌
        if l == 'X':
            visited[r][idx] = True # 돌이 있는 곳은 못가니까 방문 체크 True로 해줌

def bfs(start):
    q = deque(waters) # 물이 넘칠 예정인 위치에 고슴도치가 가면 안되므로, 큐에 물 좌표들 먼저 담기
    q.append(start) # 물 다 담고나서 고슴도치 위치 담기
    q.append('day') # 날짜 체크용 변수 담기
    day = 1

    while q:
        pop = q.popleft()
        if pop == 'day': # 하루가 끝났으면 날짜 카운트
            day += 1
            continue

        around = []
        if pop[0] > 0:
            around.append([pop[0] - 1, pop[1]])
        if pop[0] < R - 1:
            around.append([pop[0] + 1, pop[1]])
        if pop[1] > 0:
            around.append([pop[0], pop[1] - 1])
        if pop[1] < C - 1:
            around.append([pop[0], pop[1] + 1])

        for a in around:
            if mountain_map[pop[0]][pop[1]] == '*': # 만약 pop된 원소가 물의 좌표라면
                if not visited[a[0]][a[1]] and mountain_map[a[0]][a[1]] != 'D': # 물이 이동할 수 있는 위치면
                    # print('물이 넘침 ', a)
                    mountain_map[a[0]][a[1]] = '*' # 지도 정보 변경
                    visited[a[0]][a[1]] = True # 방문 체크
                    q.append(a) # 큐에 넣기
            else: # pop된 원소가 고슴도치의 좌표라면
                if not visited[a[0]][a[1]]: # 고슴도치가 갈 수 있는 좌표라면
                    visited[a[0]][a[1]] = True 
                    if mountain_map[a[0]][a[1]] == 'D': # 만약 갈 수 있는 좌표가 도착지라면
                        print(day) # 갈 때까지 걸린 날짜 출력
                        return True
                    q.append(a)
        if len(q) > 1 and q[0] == 'day': # 하루가 끝나면 또 하루를 확인할 변수 넣기
            q.append('day')
            
if not bfs(s):
    print('KAKTUS') # 끝까지 도착 못하면 KAKTUS 출력