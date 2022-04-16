import sys
from collections import deque

sys.stdin = open('sample.txt')
input = sys.stdin.readline


N, M = map(int, input().split())    #N명의 학생, M번 비교

graph = [ [] for i in range(N+1)]
degree = [0] * (N+1)


def top_sort() :

    q = deque()
    arr = []
    for i in range(1, len(degree)):       #인덱스 0은 생략
        if degree[i] == 0:
            q.append(i)         #진입 차수가 0인거 다 큐에 넣고 돌리기
   
    while q:

        now = q.popleft()
        arr.append(now)    #진입차수 0인거 꺼내서 배열에 넣어주기

        for i in graph[now]:

            degree[i] -= 1     #진입차수 하나씩 줄여주기

            if degree[i] == 0 :
                q.append(i)
                

    for i in arr :
        print(i, end=' ')


    

for i in range(M):
    a, b = map(int, input().split())

    graph[a].append(b)
    degree[b] +=1

top_sort()