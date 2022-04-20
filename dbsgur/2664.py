import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())

man, woman = map(int, input().split())

m = int(input())

realations = [[] for _ in range(n+1)]
visited = [-1] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    realations[a].append(b)
    realations[b].append(a)


def bfs():
    dq = deque()
    dq.append((man))
    visited[man] = 0
    while dq:
        m = dq.popleft()
        if m == woman:
            return
        for wm in realations[m]:
            if visited[wm] == -1:
                visited[wm] = visited[m] + 1
                dq.append((wm))


bfs()
print(visited[woman])
