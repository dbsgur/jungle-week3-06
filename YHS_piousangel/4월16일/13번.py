import sys
from collections import deque
sys.stdin = open('sample.txt')
input = sys.stdin.readline

row, col = map(int, input().split())


dx = [1,-1,0,0]
dy = [0,0,1,-1]

board = [ list(input().rstrip()) for i in range(row)]
visited = [[-1]*col for i in range(row)]
# print(board)
# print(visited)
q = deque()

def bfs(board, visited):
    
    visited[0][0] = 1
    q.append([0,0])

    while q :

        y, x = q.popleft()
        print(y, x)

        if y == row -1 and x == col -1 :
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # print(nx, ny)
            if 0<= nx < col and 0 <= ny < row  :
                if visited[ny][nx] == -1 and board[ny][nx] == '1':
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([ny,nx])
                
       


bfs(board, visited)

print(visited[-1][-1])

