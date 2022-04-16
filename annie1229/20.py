# 20. 줄 세우기(#2252)
import sys
from collections import deque

sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split()) # N: 학생수, M: 비교 횟수
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s1, s2 = map(int, sys.stdin.readline().split()) # 학생 키 비교 결과에 따라 간선 추가
    graph[s1].append(s2)
    indegree[s2] += 1 # 키가 큰 학생 진입차수 증가

def topology_sort():
    result = []
    q = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0: # 진입차수 0인 학생들 큐에 넣기
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now) 
        for g in graph[now]: # 진입차수가 0인 학생들보다 키가 큰 학생들 돌면서
            indegree[g] -= 1 # 진입차수 1개씩 감소
            if indegree[g] == 0: # 진입차수가 0이된 학생이 있으면 큐에 넣기
                q.append(g)

    print(' '.join(list(map(str, result))))

topology_sort()
