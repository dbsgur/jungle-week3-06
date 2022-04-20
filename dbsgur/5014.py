import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline
# 총 F층, S층 (현재 위치), G층 (목표 위치)
F, S, G, U, D = map(int, input().split())

# print(F, S, G, U, D)

visited = [-1 for _ in range(F+1)]


def bfs():
    dq = deque()
    dq.append((S))
    visited[S] = 0
    while dq:
        f = dq.popleft()
        if f == G:
            print(visited[f])
            return
        for nf in (f+U, f-D):
            if nf > 0 and nf <= F and visited[nf] == -1:
                dq.append((nf))
                visited[nf] = visited[f] + 1
    print("use the stairs")


bfs()
