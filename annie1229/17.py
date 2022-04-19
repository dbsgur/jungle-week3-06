# 17. 토마토(#7569)
import sys
from collections import deque
sys.stdin = open('input.txt')

M, N, H = map(int, sys.stdin.readline().split())
box = [] # 토마토 정보 담을 배열
checked = [] # 토마토 익었는지 확인 할 배열
already = [] # 이미 익어있는 토마토 담을 배열
day = -1 # 토마토가 익을 때까지 얼마나 걸리는지 확인용 변수

for h in range(H): # 박스 높이 만큼 반복
    floor = [] # 토마토 박스 한 층에 대한 정보를 담을 배열
    check = [] # 토마토 박스 한 층에 대한 체크 정보를 담을 배열
    for n in range(N): # 한 층에 행만큼 반복
        line = list(map(int, sys.stdin.readline().split()))
        floor.append(line)
        check.append([False for _ in range(M)])
        for idx, tomato in enumerate(line): # 한 행에 있는 토마토 정보 체크
            if tomato == 1: # 이미 익어있는 토마토면
                already.append([h, n, idx]) # already 배열에 위치 정보 넣어주고
                check[n][idx] = True # 이미 익었으니 True로 바꿔줌
            if tomato == -1: # 토마토가 없는 위치면
                check[n][idx] = True # 비어있는 칸이니까 True로 바꿔줌
    box.append(floor)
    checked.append(check)

def bfs(start):
    global day
    q = deque(start)
    q.append('day') # 0번째 날 확인할 위치들 다 넣었으면 날짜 변경 감지할 수 있도록 확인용 문자열 넣어주기
    
    while q:
        pop = q.popleft()
        if pop == 'day': # 만약 하루가 끝났다면
            day += 1 # 날짜 증가 시키고 다음으로 건너뛰기
            continue 

        nbox = pop[0] # 토마토가 몇번째 박스에 있는지
        py = pop[1] # 토마토가 몇번째 행에 있는지
        px = pop[2] # 토마토가 몇번째 열에 있는지

        around = []
        if nbox < H - 1:
            # print('아래에 박스에 있는 토마토', [nbox + 1, py, px])
            around.append([nbox + 1, py, px])
        if nbox > 0:
            # print('윗 박스에 있는 토마토', [nbox - 1, py, px])
            around.append([nbox - 1, py, px])
        if px < M - 1:
            # print('오른쪽에 있는 토마토', [nbox, py, px + 1])
            around.append([nbox, py, px + 1])
        if px > 0:
            # print('왼쪽에 있는 토마토', [nbox, py, px - 1])
            around.append([nbox, py, px - 1])
        if py < N - 1:
            # print('아래에 있는 토마토', [nbox, py + 1, px])
            around.append([nbox, py + 1, px])
        if py > 0:
            # print('위에 있는 토마토', [nbox, py - 1, px])
            around.append([nbox, py - 1, px])

        # print(pop, around)
        for i in around: # 주변에 익을 수 있는 토마토 위치들 돌기
            # print('visited', i[0], i[1], i[2])
            if not checked[i[0]][i[1]][i[2]]: # 아직 안익은 토마토가 있다면
                checked[i[0]][i[1]][i[2]] = True # 익은걸로 바꿔주고
                q.append(i) # 큐에 넣기
        if q[0] == 'day' and len(q) > 1: # 만약 다음 턴에 'day'가 pop 된다는 거는 하루가 끝났다는 얘기니까 'day' 문자열 넣어주기
            q.append('day') # 길이가 1보다 큰지 확인하는거는 마지막날 'day'가 연속으로 두개 들어가는걸 막기 위해서
        
bfs(already)

for check in checked:
    for c in check:
        if c.count(False): # 아직 익지 않은 토마토가 있다면 -1 출력
            print(-1)
            exit(0)
# print('토마토가 다 익었습니다!', day)
print(day)

