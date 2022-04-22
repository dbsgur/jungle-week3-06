import sys
from collections import deque

sys.stdin = open("input.txt")
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

indegree = [0] * (N+1)

for _ in range(M):
    singers = [int(x) for x in input().strip().split()]
    for i in range(1, singers[0]):
        graph[singers[i]].append(singers[i+1])
        indegree[singers[i+1]] += 1


def topology():
    result = []
    dq = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            dq.append(i)

    while dq:
        node = dq.popleft()
        result.append(node)
        for next in graph[node]:
            indegree[next] -= 1
            if indegree[next] == 0:
                dq.append(next)

    if len(result) != N:
        print(0)
    else:
        print(*result, sep='\n')


topology()
