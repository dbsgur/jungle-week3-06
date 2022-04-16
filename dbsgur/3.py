# 프림 알고리즘은 다익스트라 알고리즘과 거의 유사하다고 생각합니다.
# 차이점은 프림 알고리즘은 인접 간선을 추출하여 우선순위 큐에 삽입할 때,
# 순환이 발생하면 안되므로 방문한 노드인지 확인을 하고 우선순위 큐에 삽입을 합니다.
import heapq
import collections
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())  # 노드 수, 간선 수
graph = collections.defaultdict(list)  # 빈 그래프 생성
visited = [0] * (n+1)  # 노드의 방문 정보 초기화

# 무방향 그래프 생성
for i in range(m):  # 간성 정보 입력 받기
    u, v, weight = map(int, input().split())
    graph[u].append([weight, u, v])
    graph[v].append([weight, v, u])


# 프림 알고리즘
def prim(graph, start_node):
    visited[start_node] = 1  # 방문 갱신
    candidate = graph[start_node]  # 인접 간선 추출
    heapq.heapify(candidate)  # 우선순위 큐 생성
    mst = []  # mst
    total_weight = 0  # 전체 가중치

    while candidate:
        weight, u, v = heapq.heappop(candidate)  # 가중치가 가장 적은 간선 추출
        if visited[v] == 0:  # 방문하지 않았다면
            visited[v] = 1  # 방문 갱신
            mst.append((u, v))  # mst 삽입
            total_weight += weight  # 전체 가중치 갱신

            for edge in graph[v]:  # 다음 인접 간선 탐색
                if visited[edge[2]] == 0:  # 방문한 노드가 아니라면, (순환 방지)
                    heapq.heappush(candidate, edge)  # 우선순위 큐에 edge 삽입

    return total_weight


print(prim(graph, 1))


# 크루스컬 알고리즘
# 같은 부모인애를 찾는다.
# 부모 밑에 자식들과 연결된 선에서 가장 작은 간선을 선택한다.
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def make_union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


V, E = map(int, input().split())
graph_all = []

parent = [0] * (V + 1)
for i in range(V + 1):
    parent[i] = i

for _ in range(E):
    A, B, C = map(int, input().split())
    graph_all.append([C, A, B])


graph_all.sort()
count = 0
answer = 0

while graph_all:
    if count == (V-1):
        break

    C, A, B = graph_all.pop(0)

    if find_parent(parent, A) == find_parent(parent, B):
        continue
    else:
        make_union(parent, A, B)
        count += 1
        answer += C
print(answer)
