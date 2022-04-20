import sys
from collections import deque

sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
# ballons[좌표] = 높이
balloons = [int(x) for x in input().strip().split()]
# visited[좌표] = 방문여부
visited = [False for _ in range(N)]

# time over


def bfs(x):
    dq = deque()
    visited[x] = True
    dq.append((x))
    while dq:
        sx = dq.popleft()
        nh = balloons[sx] - 1
        # 포문 돌 때 또 있나 확인 how ? 2중 포문?
        for i in range(x+1, N):
            if visited[i] == False and balloons[i] == nh:
                dq.append((i))
                visited[i] = True


maxB = max(balloons)
maxI = balloons.index(maxB)

bfs(0)
if maxI != 0:
    bfs(maxI)

count = 2
#
for i in range(N):
    # i보다 크다 또 출발
    if visited[i] == False:
        bfs(i)
        count += 1

print(count)

# time over. ...
# max height부터 시작해보자
# ? 뒤에 나보다 작은애가 있나 판단

# correct CODE


n = int(sys.stdin.readline())
h = list(map(int, sys.stdin.readline().split()))
# 발사된 각 화살의 높이
cnt = [0] * (n + 1)

# 화살의 높이를 확인한다.
for i in h:
    # 화살이 발사되어있으면 똑같은 화살로 풍선을 터트리고 화살의 높이를 내린다.
    if cnt[i] > 0:
        # 풍선을 터트리고 원래 화살을 빼주고
        # 화살의 높이 -1 위치에 화살을 다시 조준한다.
        cnt[i] -= 1
        cnt[i - 1] += 1
    else:
        # 화살이 발사되지 않았으므로
        # 풍선을 터트리고 화살의 높이 -1 위치에 화살을 조준한다.
        cnt[i - 1] += 1

# 발사된 화살의 개수를 출력한다.
print(sum(cnt))
