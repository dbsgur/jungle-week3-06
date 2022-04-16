import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('sample.txt')

input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]
parent_node = [0] * (n+1)
for i in range(n-1):

    a, b = map(int, input().split())

    tree[a].append(b)
    tree[b].append(a)

def dfs(tree, parent_node, root):               # 처음에 트리의 루트를 1이라고 설정해줘서 이게 성립가능 (각각의 트리의 루트는 단 하나!)

    for i in range(len(tree[root])):
        if parent_node[tree[root][i]] == 0 :
            parent_node[tree[root][i]] = root
            dfs(tree, parent_node, tree[root][i])

dfs(tree, parent_node, 1)
for i in range(2,len(parent_node)):
    print(parent_node[i])