import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

idx = 0
tree = []
while True :
    node = input()            #찾아보니까 try except로도 처리를 해주네요
    if node == "":
        break
    node = int(node)
    tree.append(node)
    idx += 1


def dfs(start, end):

    if start >= end :
        return
    
    root = tree[start]
    idx = 0

    if tree[end-1] <= root :         #왼쪽 트리만 있을때
        dfs(start+1, end)
        print(root)
        return
    
    for i in range(start+1, end):    # 왼쪽 트리에서 오른쪽 트리로 넘어가는 인덱스
        if tree[i] > root :
            idx = i
            break

    dfs(start+1, idx)                
    dfs(idx, end)
    print(root)      

dfs(0, len(tree))


