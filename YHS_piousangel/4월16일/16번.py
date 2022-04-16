import sys
from collections import deque
sys.stdin = open('sample.txt')

input = sys.stdin.readline

n = int(input())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(board, visited):

    q = deque()
    visited[0][0]  = 0
    q.append([0, 0])

    while q :

        y, x = q.popleft()
        # print("y,x좌표: ", y,x)
      
        if y == n-1 and x == n-1:
            print(visited[-1][-1])
            return

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < n and 0 <= ny < n :
                if visited[ny][nx] == -1 and board[ny][nx] == 1:
                    visited[ny][nx] = visited[y][x]
                    q.appendleft([ny, nx])
                 
                elif visited[ny][nx] == -1 and board[ny][nx] == 0 :     
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([ny, nx])


board = [ list(map(int, input().rstrip())) for _ in range(n)]
visited = [ [-1] * n for _ in range(n)]
bfs(board, visited)

