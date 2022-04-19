import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
check = [0 for _ in range(k+1)]
# print(coins)
# bfs

flag = True


def bfs():
    global flag
    dq = deque()
    for coin in coins:
        if coin > k:
            continue
        dq.append((coin, 1))
        check[coin] = 1
    while dq:
        val, cnt = dq.popleft()
        if val == k:
            print(cnt)
            flag = False
            break
        for coin in coins:
            if val + coin > k:
                continue
            if check[val+coin] == 0:
                check[val+coin] = 1
                dq.append((val+coin, cnt+1))


bfs()

if flag:
    print(-1)

# dynamic programming
# dp = [10001 for _ in range(k+1)]
# dp[0] = 0
# for i in range(n):
#     for j in range(coins[i], k+1):
#         dp[j] = min(dp[j], dp[j-coins[i]] + 1)

# if dp[-1] != 10001:
#     print(dp[-1])
#     # break
# else:
#     print('-1')
