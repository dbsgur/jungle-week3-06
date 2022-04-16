import sys
from collections import deque

sys.stdin = open("input.txt")

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

# 진입차수
indegree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    # graph[b].append(a)
    indegree[b] += 1


def topology():
    result = []
    q = deque()
    # 초기에 진입차수 0인 노드들 큐에 넣기
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌때까지 반복
    while q:
        node = q.popleft()
        # 꺼낸 원소는 위상 정렬 결과값에 append
        result.append(node)
        # 꺼낸 노드랑 연결된 노드들 검색
        for next in graph[node]:
            indegree[next] -= 1
            # 새롭게 진입차수가 0이 된 노드들 큐에 넣기
            if indegree[next] == 0:
                q.append(next)
    for i in result:
        print(f"{i}", end=' ')


topology()
