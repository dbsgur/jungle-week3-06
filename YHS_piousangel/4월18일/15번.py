import sys
import heapq
from collections import deque

# int(1e9)
INF = sys.maxsize    #2147483647 Int형에서 최댓값 

sys.stdin = open('sample.txt')    
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [ [] for _ in range(N+1)]


for i in range(M):

    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])


start_num, end_num = map(int, input().split())


def bfs(graph, start_num, end_num) :
    global distance
    q = []

    heapq.heappush(q, (start_num, 0))
    q.append([start_num, 0])
    # visited[start_num] = True

    while q :
        # print("q! :", q)
        now, now_cost = heapq.heappop(q)

        # now, cost = q.popleft()

        # if now == end_num :
        #     # min_num = min(cost, min_num)
        #     print(cost)

        for node in graph[now_cost] :
            cost = now_cost + node[1]
            if distance[node[0]] > cost:
                distance[node[0]] = cost
                heapq.heappush(q, (node[0], cost))
            # q.append([node[0], cost + node[1]])
            # heapq.push(q, cost,node)
                




bfs(graph, start_num, end_num)
print(distance)