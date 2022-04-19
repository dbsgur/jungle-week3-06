# 11. 빙산(#2573) #정답 코드 (https://deok2kim.tistory.com/247)
import sys
sys.setrecursionlimit(10**9) # RecursionError 방지
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
year = 0 # 몇년 지났는지 count

iceberg = [] # 빙산 정보 담을 배열
ices = [] # 높이가 1이상인 빙산들 위치 담을 배열
for n in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    iceberg.append(line)
    for m, l in enumerate(line):
        if l > 0:
            ices.append((n, m))

def melting():
    melting_area = {}  # 녹일 곳
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[0] * M for _ in range(N)]  # 방문
    stack = []
    stack.append(ices[0]) # 탐색할 첫 빙산 넣어주기
    selected_iceberg = 0  # 선택된 빙산들 ( 나중에 전체 빙산과 비교해서 한덩어리인지 확인 )
    visited[ices[0][0]][ices[0][1]] = 1
    while stack:
        x, y = stack.pop()
        selected_iceberg += 1
        melting_cnt = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if iceberg[nx][ny] and not visited[nx][ny]:  # 옆이 육지이면 다음 탐색
                stack.append((nx, ny)) 
                visited[nx][ny] = 1
            elif iceberg[nx][ny] == 0:  # 옆이 바다이면 녹이는 카운트
                melting_cnt += 1

        melting_area[(x, y)] = melting_cnt # dict에 저장

    # 녹이기
    new_iceberg = []  # 새로운 빙산으로 바꾸기 위해
    for key, value in melting_area.items():
        i, j = key
        iceberg[i][j] = max(0, iceberg[i][j] - value) # 만약 연산 결과가 음수면 0으로
        if iceberg[i][j] > 0: # 아직 높이가 남아있으면
            new_iceberg.append((i, j)) # 새로운 빙산 리스트에 추가

    return selected_iceberg, new_iceberg # 탐색한 빙산 갯수, 새로운 빙산 배열 리턴

while True:
    selected_cnt, new_ices = melting()

    if selected_cnt != len(ices): # 카운트한 빙산의 수가 원래 빙산의 수랑 다르면 한덩어리가 아니라는거
        break
    if selected_cnt == 0 or len(new_ices) == 0: # 빙산이 없으면 덩어리가 나뉘지 않고 빙산이 다 녹은거니까 0 출력
        year = 0
        break
    ices = new_ices[:] # 남아있는 빙산 배열 갱신

    year += 1
    
print(year)