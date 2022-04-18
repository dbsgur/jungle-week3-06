import sys
from collections import deque
sys.stdin = open('sample.txt')

input = sys.stdin.readline

row, col = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]



q = deque()
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] != 0 :
            q.append([i,j, board[i][j]])


def bfs(board, visited) :

    y, x, life = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < col and 0 <= ny < row :
            if board[nx][ny] == 0 :
                life -= 1
            elif 



    

while True:          # 두 부
    
    if

    visited = [ [False] * col for _ in range(row) ]
    bfs(board, visted)
    

