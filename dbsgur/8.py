import sys

sys.setrecursionlimit(10**9)
sys.stdin = open("input.txt")
input = sys.stdin.readline


def dfs(parent):
    global flag
    if color[parent] == 0:
        color[parent] = 1
    pColor = color[parent]
    for i in graphs[parent]:
        if not color[i]:
            if pColor == 1:
                color[i] = 2
            elif pColor == 2:
                color[i] = 1
            dfs(i)
        elif color[i] == pColor:
            # print("NO")
            # print("color = pColor")
            flag = False
            return
    # print("end")

    return


K = int(input())


for _ in range(K):
    V, E = map(int, input().split())
    flag = True
    graphs = [[]for _ in range(V+1)]

    color = [0] * (V+1)

    for i in range(E):
        u, v = map(int, input().split())
        graphs[u].append(v)
        graphs[v].append(u)
    for i in range(1, V+1):
        if not color[i]:
            dfs(i)
            # print(flag)

    # print(f"flag: {flag}")
    if flag:
        print("YES")
    else:
        print("NO")
