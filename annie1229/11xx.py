# 11. 빙산(#2573) # 시간 초과 코드
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

def dfs(sx, sy, visited):
    visited[sx][sy] = True

    around = []
    if sy > 1:
        around.append([sx, sy - 1])
    if sy < M - 2:
        around.append([sx, sy + 1])
    if sx > 1:
        around.append([sx - 1, sy])
    if sx < N - 2:
        around.append([sx + 1, sy])

    for a in around:
        ax = a[0]
        ay = a[1]
        if not visited[ax][ay] and iceberg[ax][ay]: # 주변에 아직 빙산이 남아있으면 계속 dfs
            dfs(ax, ay, visited)

def isConnect(): # 빙산이 한덩어리인지 확인하는 함수
    visited = [[False for _ in range(M)] for _ in range(N)]
    count = 0 # 빙산이 몇개의 그룹인지 확인할 변수
    for ice in ices:
        i = ice[0]
        j = ice[1]
        if not visited[i][j]:
            count += 1
            if count > 1: # 계속 시간초과 나길래...일단 2개 이상 나오면 무조건 리턴하도록 추가해봤다.
                return 2
            dfs(i, j, visited)
    return count

def decreaseIceberg(i, j): # 주변의 바닷물 몇칸있는지 확인하는 함수
    decrease = 0
    if j > 0:
        if iceberg[i][j - 1] == 0:
            decrease += 1
    if j < M - 1:
        if iceberg[i][j + 1] == 0:
            decrease += 1
    if i > 0:
        if iceberg[i - 1][j] == 0:
            decrease += 1
    if i < N - 1:
        if iceberg[i + 1][j] == 0:
            decrease += 1
    return decrease

isSame = True # 처음에는 무조건 한덩어리니까 isConnect 실행할 필요 없음

while True:
    if not isSame:
        cnt = isConnect()

        if cnt > 1: # 두덩어리 이상이면 출력하고 종료
            print(year)
            exit(0)
        if cnt == 0: # 아무것도 없으면 0출력하고 종료
            print(0)
            exit(0)
    year += 1
    
    temp = []
    new_ices = []

    for ice in ices: # 높이 있는 빙산들 돌기
        i = ice[0]
        j = ice[1]
        dec = max(iceberg[i][j] - decreaseIceberg(i, j), 0)
        temp.append([i, j, dec]) # 변화된 빙산 정보 담기
        if dec > 0: # 아직 높이가 남아있는 빙산이면 new_ices배열에 추가
            new_ices.append(ice)
    if ices == new_ices: # 이전 빙산과 현재 빙산의 위치들이 똑같으면 한덩어리인지 확인할 필요 없음
        isSame = True
    else: # 다르면 한덩어리인지 확인해야함
        isSame = False
    ices = new_ices # 높이 남아있는 빙산 배열 갱신

    for t in temp: # 변화된 빙산값들을 갱신
        iceberg[t[0]][t[1]] = t[2]
    