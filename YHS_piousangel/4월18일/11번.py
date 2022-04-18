import sys
sys.stdin = open('sample.txt')

input = sys.stdin.readline

row, col = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(row)]




def dfs(board, visited, y, x, 0) :

    # for i in range(len(board)) :
    #     for j in range(len(board[0])):

    # 4면중 0개수 체크
            



max_value = 0
y = 0
x = 0
for i in range(len(board)):
    for j in range(len(board[0])):
        max_value = max(board[i][j], max_value)

for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == max_value :
            y = i
            x = j

dfs(board, visited, y, x, 0)
