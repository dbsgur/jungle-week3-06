# first TRY - DFS : 시간초과
# second TRY - BFS : 시간초과
# third TRY - 다익스트라(feat, annie1229) : 시간초과
# forth TRY - 다익스트라 + 예외처리(feat, annie1229) : 무한루프
# fifth TRY - 4번 수정 : 왜틀린지 모르겠음
# sisth TRY - 답 보기 :

import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())

M = int(input())

graph = [[100001]*(N+1) for _ in range(N+1)]
#visited = [False] * (N+1)

for _ in range(M):
    start, end, cost = map(int, input().split())
    if graph[start][end]:
        graph[start][end] = min(graph[start][end], cost)


print(graph)

# start, end가 같고 cost가 다른 버스가 있다...!!
# 가장 비용이 낮은 것만 넣어야한다. feat, annie
# 튜플은 변경하거나 삭제할수 없다.
# 그래서 튜플보다 배열을  사용해야할 것 같다.
# graph[start].append([end, cost])
# 여기서 배열을 사용하는 것이 아니라 튜플에서 뺄때 heap을 쓰는 것도 방법....

startCity, endCity = map(int, input().split())


def bfs(start):
    costs = [sys.maxsize for _ in range(N + 1)]
    # costs = []  # 비용 담을 배열
    # for _ in range(N+1):
    #     costs.append(sys.maxsize)
    dq = deque([start])
    # dq.append(start)
    costs[start] = 0
    while dq:
        nowCity = dq.popleft()
        for next, cost in enumerate(graph[nowCity]):
            if cost != 100001:
                if costs[next] > costs[nowCity] + cost:
                    costs[next] = costs[nowCity] + cost
                    dq.append(next)

        # for i in range(N+1):
        #     if graph[nowCity][i] and costs[i] > costs[nowCity] + graph[nowCity][i]:
        #         costs[i] = costs[nowCity] + graph[nowCity][i]
        #         dq.append(i)
    # print(costs)
    return costs[endCity]


print(bfs(startCity))

# 특정 경로 탐색 문제다.
# dfs로 풀어야한다.
# 놀랍게도 아니었다 !
# 최소 비용 -> bfs!
# 시간 초과가 납니당

# costs = 1e9

# def dfs(n, c):
#     # if) n == endCity : cost 저장
#     global costs
#     if n == endCity:
#         costs = min(c, costs)

#     if c >= costs:
#         return
#     for next, cost in graph[n]:
#         if visited[next] == False:
#             # print(f"next: {next}")
#             # print(f"cost: {cost}")
#             # move
#             visited[next] = True
#             dfs(next, cost+c)
#             visited[next] = False

# visited[startCity] = True
# dfs(startCity, 0)
# # print(f"costs : {costs}")
# print(costs)


# 다른사람 풀이
# import sys
# import heapq
# INF = sys.maxsize
# input = sys.stdin.readline

# def dijkstra(start_cost,start_node):
#     dist = [ INF for _ in range(n+1)]
#     dist[start_node] = 0
#     q = [(start_cost,start_node)]

#     while q:
#         print(dist)
#         p = heapq.heappop(q)
#         cur_cost, cur_node = p[0], p[1]
#         for next_cost, next_node in graph[cur_node]:
#             if dist[next_node] > cur_cost + next_cost:
#                 dist[next_node] = cur_cost + next_cost
#                 heapq.heappush(q, (dist[next_node],next_node))
#     return dist

# # 도시 개수 n, 버스 개수 m
# n = int(input().rstrip())
# m = int(input().rstrip())

# graph = [ [] for _ in range(n+1) ]

# for _ in range(m):
#     start,end,cost = map(int,input().rstrip().rsplit())
#     graph[start].append((cost,end))

# want1, want2 = map(int,input().rstrip().rsplit())
# answer = dijkstra(0,want1)
# print(answer[want2])
