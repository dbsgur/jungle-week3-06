# 8. 이분 그래프(#1707)
import sys
sys.setrecursionlimit(10**9) # 재귀 깊이 늘려주기
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())
flag = True

def dfs(graph, idx, color):
    global visited # 방문 여부 확인하는 배열
    global check   # 노드이 색을 저장하는 배열

    visited[idx] = True

	# 연결된 이전 노드와 반대되는 색으로 설정
    if color == 'R': 
        check[idx] = 'B'
        color = 'B'
    else:
        check[idx] = 'R'
        color = 'R'

    for i in graph[idx]:
        if not visited[i]:
            dfs(graph, i, color)


for _ in range(T):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        A, B = map(int, sys.stdin.readline().split())
		# 인접리스트로 그래프 표현
        graph[A].append(B)
        graph[B].append(A)

    visited = [False for _ in range(V + 1)]
    check = ['' for _ in range(V + 1)]
    dfs(graph, 1, 'R')

    for b, g in enumerate(graph):
        for a in g:
            if not visited[a]: # 아직 방문하지 않은 노드있으면 탐색하기
                dfs(graph, a, 'R')
            if check[a] == check[b]: # 인접한 노드끼리 색이 같으면 flag False로
                flag = False
    if flag:
        print('YES')
    else:
        print('NO')
    flag = True