# O(N)풀이 - 블로그참조 https://kth990303.tistory.com/141
# 실내 - 실내이면서, 중간에 실내를 거치지 않는 길의 개수를 구하는 문제
# 실외를 하나의 컴포넌트로 생각하여, 그 주변에 인접한 실내의 개수를 dfs로 count해준다.
# 또한, 실내-실내 길 사이에 실외가 하나도 없는 경우는 위 방법으로 카운트 되지 않으므로 실내이면서 주변 인접 실내인 경우를 count해준다.

# 위와같이하면 1번부터 N번까지 탐색 O(N),
# 중간에 DFS가 있긴 하지만, i번에서 DFS로 i~j번까지 탐색한다고 치면,
# 이후에, i+1 ~ j번까진 이미 DFS로 탐색했기 때문에 추가적으로 탐색할 필요가 없으므로
# 결과적으로 O(N)의 시간복잡도로 처리할 수 있다.

# 즉, 인접한 실외를 한덩어리로 보고 그 덩어리에 인접한 실내의 수 n을 구하고
# 각 덩어리별로 n*(n-1)의 경우의수를 계산
# +
# 각 실내별 인접한 실내 구하기

import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

numVertices = int(input())
col = list(map(int, list("0"+input().strip())))

graph = [[] for _ in range(numVertices + 1)]

for _ in range(1, numVertices):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


def calPaths(graph: list, col: list) -> int:
    count = 0
    visited = set()
    # 실외의 인접 실내 갯수 구하기

    def dfs(exterior: int) -> int:
        cnt = 0
        for neighbor in graph[exterior]:
            if col[neighbor] == 1:
                cnt += 1
            else:
                if neighbor not in visited:
                    visited.add(neighbor)
                    cnt += dfs(neighbor)
        return cnt

    for i in range(1, numVertices + 1):
        # 각 실내별 인접한 실내 구하기
        if col[i] == 1:
            for j in graph[i]:
                if col[j] == 1:
                    count += 1
        # 인접한 실외를 한 덩어리로 보고 그 덩어리에 인접한 실내의 수를 구한 뒤
        # 각 덩어리별로 n*(n-1)의 경우의 수를 계산
        else:
            if i not in visited:
                visited.add(i)
                tmp = dfs(i)
                count += tmp * (tmp - 1)

    return count


print(calPaths(graph, col))


# idea : 실내(A[i] == 0) 출발 -> (실외(A[i] == 1) 경유) -> 실내 도착
# 이 방법은 나의 풀이였다. O(N^2)기때문에 108점 받는다.

# import sys
# from collections import deque

# sys.stdin = open("input.txt")

# input = sys.stdin.readline


# N = int(input())

# A = [int(x) for x in input().strip()]

# graph = [[]for _ in range(N+1)]
# visited = [False] * (N+1)

# for i in range(N-1):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)

# count = 0


# def dfs(n, via):
#     global count
#     if len(via) > 1 and via[0] == via[-1]:
#         count += 1
#         return
#     for x in graph[n]:
#         if not visited[x]:
#           # 실내가는 경우
#           # 1. 전에 실내 -> 종료
#           # 2. 전에 실외 -> 종료
#           # if via
#             visited[x] = True
#             dfs(x, via+str(A[x-1]))
#             visited[x] = False

#         # 실외 가는 경우
#         # 1. 전에 실내 -> 출발
#         # 2. 전에 실외 -> 경유


# for i in range(N):
#     if A[i] == 1:
#         visited[i+1] = True
#         dfs(i+1, '1')
#         visited[i+1] = False

# print(count)
