import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 10**5

check = [0 for _ in range(MAX+1)]


def bfs():
    dq = deque()
    dq.append(N)
    while dq:
        x = dq.popleft()
        if x == K:
            print(check[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not check[nx]:
                check[nx] = check[x] + 1
                dq.append(nx)


bfs()
