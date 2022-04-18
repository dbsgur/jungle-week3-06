import sys
from collections import deque

sys.stdin = open('sample.txt')
input = sys.stdin.readline

dx = [0,0,0,0,1,-1]
dy = [0,0,1,-1,0,0]
dz = [1,-1,0,0,0,0]

y, x, z = map(int, input().split())


# box =  [ [[] * x for _ in range(y)] for _ in range(z) ]

box = [[] for i in range(z)]

visited = [[ [False] * y for _ in range(x)] for _ in range(z) ]

for i in range(z):
    for j in range(x):
            # box[i][j] = input().split()
            box[i].append(list(map(int, input().split())))



def bfs() :
    global answer , x, y, z
    # q = deque()
    # q.append([sh, sy, sx])
    while q :
        
        now_x, now_y, now_h = q.popleft()      #처음이라고 가정했을 때 처음 1인 것들을 다 큐에 넣었는데 그거 꺼내서 
        visited[now_h][now_x][now_h] = True

        # total = 0
        # for i in range(z):
        #     for j in range(y):
        #         for k in range(x):
        #             total += int(box[i][j][k])

        # if total == x*y*z:
        #     return

        for i in range(6) :

            nh = now_h + dz[i]
            ny = now_y + dy[i]
            nx = now_x + dx[i]
            # print(nh, ny, nx)

            if 0 <= nh < z and 0 <= ny < y and 0 <= nx < x :
                # print("ok")
                if visited[nh][nx][ny] != True and box[nh][nx][ny] == 0 :
                    visited[nh][nx][ny] = True
                    box[nh][nx][ny] = box[now_h][now_x][now_y] + 1
                    q.append([nx, ny, nh])
    

answer = 0
q = deque()
for i in range(z) :
    for j in range(x):
        for k in range(y):
            if visited[i][j][k] != True and box[i][j][k] == 1:
                # bfs(box, visited, i, j, k)
                q.append([j,k,i])

bfs()
flag = False
max_num = 0
for i in range(z):
    for j in range(x):
        for k in range(y):
            if box[i][j][k] == 0:
                flag = True
            max_num = max(max_num, box[i][j][k])

if flag :
    print("-1")
else:
    print(max_num-1)