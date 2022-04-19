import sys
import heapq
sys.stdin = open('sample.txt')
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
arr = [INF] * (N+1)               # 출발점에서 시작해서 도착지로 가는 cost 최소가 나올 때 마다 계속 갱신해줘요!

for i in range(M):
    A, B, cost = map(int, input().split())
    graph[A].append((B, cost))

start_num, end_num = map(int, input().split())


def bfs(graph, arr, start_num) :

    q = []
    arr[start_num] = 0
    heapq.heappush(q, (0, start_num))

    while q :

        now_cost, pos = heapq.heappop(q)

        for node in graph[pos] :
            cost = now_cost + node[1]

            if arr[node[0]] > cost :
                arr[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))          #최소힙을 이용해서 cost가 낮은 것 부터 꺼내고싶어요

bfs(graph, arr, start_num)
print(arr[end_num])