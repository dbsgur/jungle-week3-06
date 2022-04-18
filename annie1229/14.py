# 14. 특정 거리의 도시 찾기(#18352)
import sys
from collections import deque
sys.stdin = open('input.txt')

N, M, K, X = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)

def bfs(start):
    visited = [[] for _ in range(N + 1)]
    queue = deque([start])
    visited[start] = True
    check = [[] for _ in range(N + 1)]
    cost = 0
    check[0].append(start)

    while queue:
        pop = queue.popleft()
        
        if check[cost] and pop == check[cost][0]:
            cost += 1
        for i in graph[pop]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                check[cost].append(i)

    if check[K]:
        check[K].sort() # 6퍼쯤에서 틀렸습니다 나왔었는데, 반례에 출력할 때 정렬해서 출력하면 통과된다고 해서 추가했더니 한 20퍼까지 가더라
        for n in check[K]:
            print(n)
    else:
        print(-1)

bfs(X)



