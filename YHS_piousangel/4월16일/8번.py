import sys
from collections import deque

sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())

def dfs(v, group):    #처음에 : 받아온 방문하지 않은 곳, 그룹 1

    visited[v] = group # 그룹 1로 지정
    
    for i in graph[v]:
        if visited[i] == 0:
            if not dfs(i, -group):      #1, -1 부호 바꿔주면서 chk
                return False
        elif visited[i] == visited[v]:
            return False
    return True

for i in range(n):
    v, e = map(int, input().split())
    graph = [ [] for _ in range(v+1)]
    visited = [0] * (v+1)
    for i in range(e):
        a, b = map(int, input().split())

        graph[a].append(b)
        graph[b].append(a)
    
    chkGraph = True
    
    for i in range(1, v+1):
        if visited[i] == 0 :
            chkGraph = dfs(i, 1)
            if chkGraph == False:     #break 안걸면 다시 True로 바뀔수 있어요
                break
            
    if chkGraph:
        print("YES")
    else:
        print("NO")

        


