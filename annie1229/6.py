# 6. 바이러스(#2606)
import sys
sys.stdin = open('input.txt')

V = int(sys.stdin.readline())
E = int(sys.stdin.readline())
network = [[] for _ in range(V + 1)]

for _ in range(E):
    c1, c2 = map(int, sys.stdin.readline().split())
    network[c1].append(c2)
    network[c2].append(c1)

def dfs(start, visited):
    visited[start] = True

    for i in network[start]:
        if not visited[i]:
            dfs(i, visited)
visited = [False for _ in range(V + 1)]
dfs(1, visited)

virus = -1 # 1번 컴퓨터는 카운팅하지 않음
for v in visited:
    if v:
        virus += 1
print(virus)

