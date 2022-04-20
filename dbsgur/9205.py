import sys
from collections import deque

sys.stdin = open("input.txt")
input = sys.stdin.readline

t = int(input())


def bfs():
    dq = deque()
    dq.append(home)
    visited = set()
    while dq:
        x, y = dq.popleft()
        if abs(x-festival[0]) + abs(y-festival[1]) <= 1000:
            return True
        for i in range(n):
            if i not in visited:
                nx, ny = gs[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    dq.append([nx, ny])
                    visited.add(i)
    return False


for _ in range(t):
    n = int(input())
    # home coordinate
    home = [int(x) for x in input().split()]
    # 편의점 좌표
    gs = [[int(x) for x in input().split()] for _ in range(n)]
    # rock festival coordinate
    festival = [int(x) for x in input().split()]

    if bfs():
        print("happy")
    else:
        print("sad")
