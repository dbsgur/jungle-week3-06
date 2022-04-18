import sys
import heapq
sys.stdin = open('sample.txt')
input = sys.stdin.readline
max_value = 100001

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]  
cost_list = [max_value] * (N+1)               # 출발점에서 시작해서 도착지로 가는 cost 최소가 나올 때 마다 계속 갱신해줘요!

for i in range(M):
    A, B, cost = map(int, input().split())
    graph[A].append((B, cost))

start_num, end_num = map(int, input().split())


def bfs(graph, cost_list, start_num) :

    q = []
    cost_list[start_num] = 0
    heapq.heappush(q, (0, start_num))

    while q :

        now_cost, pos = heapq.heappop(q)

        if cost_list[pos] < now_cost:             # 지금 코스트가 큐에서 받은 코스트 보다 작으면 그냥 컨티뉴하면서 로직 실행 X
            continue

        for node in graph[pos] :
            cost = now_cost + node[1]            # cost = 전 비용 + 연결하려는 비용

            if cost_list[node[0]] > cost :       #  기존의 비용과 비교 했을 때 기존비용이 크면 교체
                cost_list[node[0]] = cost_list
                heapq.heappush(q, (cost, node[0]))   # 힙에 넣어 꺼낼 때 최소비용이 앞에 오도록

print(graph)
bfs(graph, cost_list, start_num)
print(cost_list[end_num])