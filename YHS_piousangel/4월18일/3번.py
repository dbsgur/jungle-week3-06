import sys

sys.stdin = open('sample.txt')

input = sys.stdin.readline

V, E = map(int, input().split())


node_list = []
root_list = [i for i in range(V+1)]
cost = 0

for i in range(E):                          #root를 찾는게 중요하다

    A, B, val = map(int, input().split())

    node_list.append([A,B,val])
    
node_list.sort(key=lambda x : x[2])  #가중치로 정렬해서 낮은 가중치 부터 계산하는게 크루스칼의 핵심

def dfs(node) :
    
    if node != root_list[node]:                    #처음 1,2 는 1,2로 나가지만 2,3이 들어왔을 때 2는 1로 설정되어있기 때문에 1로, 3은 3으로 나간다. 하지만 나중에 루트가 1로 합쳐진다.
        root_list[node] = dfs(root_list[node])
    return root_list[node]
                
    
for values in node_list:

    f_node = dfs(values[0])
    s_node = dfs(values[1])

    if f_node != s_node:                   #마지막 1,3은 루트가 같아서 (계산하면 사이클이 생김)이쪽으로 안들어옴
        if sRoot > eRoot:
            root_list[f_node] = s_node
        else:
            root_list[s_node] = f_node

        cost += values[2]                   # 사이클이 안생길때만 가중치를 더해줘

print(cost)