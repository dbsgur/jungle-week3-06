import sys
from collections import deque

sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())

costs = [0]*(N+1)

graph = [[]for _ in range(N+1)]
indegree = [0] * (N+1)

for i in range(N):
    builds = [int(x) for x in input().strip().split()]
    costs[i+1] = builds[0]
    for j in range(1, len(builds) - 1):
        graph[builds[j]].append(i+1)
        # graph[builds[j]].append(i)
        indegree[i+1] += 1


def topology():
    result = [0] * (N+1)
    dq = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            dq.append(i)

    while dq:
        node = dq.popleft()
        result[node] += costs[node]
        for next in graph[node]:
            indegree[next] -= 1
            result[next] = max(result[next], result[node])
            if indegree[next] == 0:
                dq.append(next)
    return result


print(*topology()[1:], sep='\n')
# print(result)
