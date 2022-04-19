import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())   # N은 구슬 수, M은 비교한 횟수

overweight_graph = [[] for _ in range(N+1)]
lessweight_graph = [[] for _ in range(N+1)]

for i in range(M):
    high, row = map(int, input().split())

    overweight_graph[row].append(high)  # row 보다 무게가 더 많이 나가는 모음집들
    lessweight_graph[high].append(row)  # high 보다 무게가 덜 나가는 모음집들


print("보다 무게가 더 많이 나가는 모음집들", overweight_graph)
print("보다 무게가 덜 나가는 모음집들", lessweight_graph)


def bfs(idx, graph):
    cnt = 0
    q = deque()
    q.append(idx)
    visited[idx] = True
    while q:

        now_idx = q.popleft()
        
        for node in graph[now_idx] :
            if not visited[node] :
                visited[node] = True
                q.append(node)
                cnt += 1

    return cnt

ol_list = []
answer = 0
for i in range(1, N+1):
    visited = [False] * (N+1)
    # ol_list.append([bfs(i, overweight_graph), bfs(i, lessweight_graph)])
    ol_list = [bfs(i, overweight_graph), bfs(i, lessweight_graph)]
    if (N+1)//2 <= ol_list[0] or (N+1)//2 <= ol_list[1] :
        answer += 1

# answer = 0
# for arr in ol_list :
#     if (N+1)//2 <= arr[0] or (N+1)//2 <= arr[1] :
#         answer += 1
print(answer)