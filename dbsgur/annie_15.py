import sys
from collections import deque
sys.stdin = open("input.txt")
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
bus = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, cost = map(int, sys.stdin.readline().split())
    flag = True
    for idx, t in enumerate(bus[a]):
        if t[1] == b:
            flag = False
            if t[0] > cost:
                # 같은 경로에 비용이 더 작은 버스가 있으면 값 수정하기(같은 경로에 제일 작은 비용이 담기게)
                bus[a][idx] = (cost, b)
    if flag:
        bus[a].append((cost, b))
s, e = map(int, sys.stdin.readline().split())


def bfs(start, end):
    costs = [sys.maxsize for _ in range(N + 1)]  # 방문하지 않은 정점들의 비용은 무한대로
    queue = deque([start])
    costs[start] = 0  # 시작 정점은 0으로 설정
    while queue:
        pop = queue.popleft()
        for next in bus[pop]:
            if costs[next[1]] > next[0] + costs[pop]:  # 새로 이동할 노드의 비용이 현재 이동비용보다 크면 갱신해주기
                # print(next[1],‘cost 업데이트 ‘, costs[next[1]], ‘=’, next[0], ‘+’, costs[pop])
                costs[next[1]] = next[0] + costs[pop]
                # 여기가 중요! 방문체크를 안하는 대신 값이 갱신될때만 다시 큐에 넣어줘야함
                queue.append(next[1])
    print(costs[end])


bfs(s, e)
