from collections import deque
import sys
import copy

sys.stdin = open('sample.txt')
input = sys.stdin.readline

N = int(input())    #N은 완제품 1 ~ N-1 은 기본 or 중간 부품
M = int(input())  

graph = [ [] for _ in range(N+1)]   #어디서 부터 중간부품인질 몰라요
degree = [0] * (N+1)     #그래서 차수도 N+1 다 커버하게 끔


def top_sort() :

    q = deque()
    arr = [0] * len(degree)
    # arr = copy.deepcopy(degree)
    
    for i in range(1,5):
        arr[i] = degree[i]

    # print(degree)
    for i in range(1, len(degree)):
        if degree[i] == 0:
            q.append(i)              #차수가 0인거 다 넣어

    while q :

        now = q.popleft()    #차수가 0인거
 
        for i in graph[now] :

            temp = 0
            while degree[i] > 0 :
                degree[i] -=1
                arr[i] += 1
                
                for j in graph[i]:             # 중간 -> 기본으로 가기위해 예를들어 6에서 5호출 할때 5안에 있는 1,2의 진입차수를 증가시켜줬습니다. 
                    
                    degree[j] += 1              
                    arr[j] += 1
            
            q.append(i)

    for i in arr :
        print(i, end=' ')

info_list = []
for i in range(M):

    a, b, k = map(int, input().split())   #a를 만드는데 부품b가 k개 필요하다

    graph[a].append(b)
    degree[b] += k
    info_list.append([a,b,k])


print(graph)
print(degree)
print("=========")
top_sort()
print()
print(graph)
print(degree)