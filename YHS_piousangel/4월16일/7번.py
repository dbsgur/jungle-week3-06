import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]

for i in range(n-1):

    a, b = map(int, input().split())

    tree[a].append(b)
    tree[b].append(a)


visited = [False] * (n-1)


# def dfs(tree, visited, root, cnt) :
#     global root_list
#     if cnt == n-1 :
#         return

#     print(root)
    
#     for i in range(len(tree)):
#         if tree[i][0] == root and visited[i] == False:
#             visited[i] = False
#             dfs(tree, visited, tree[i][1], cnt+1)
#         elif tree[i][1] == root and visited[i] == False:
#             visited[i] = False
#             root_list.append([root, tree[i][0]])
#             dfs(tree, visited,  tree[i][0], cnt+1)
        
    
root_list = []
dfs(tree, visited, 1, 0)