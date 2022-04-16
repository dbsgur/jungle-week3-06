import sys

sys.setrecursionlimit(10**9)
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())

tree = [[]for _ in range(N+1)]

for i in range(N-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

visited = [False] * (N+1)

result = [0 for _ in range(N+1)]

# n : start = parent


def dfs(n):
    for i in tree[n]:
        if result[i] == 0:
            result[i] = n
            dfs(i)


# print(result)
dfs(1)

# print(*result)
for i in range(2, N+1):
    print(result[i])
