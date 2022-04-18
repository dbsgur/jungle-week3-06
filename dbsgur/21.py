import sys
from collections import deque

sys.stdin = open("input.txt")

input = sys.stdin.readline

N = int(input())

M = int(input())

# 내 처음 생각은 needs에 연결 정보를 받아서 중간제품 될수록 업데이트를 해주려고 했다.
# 근데, 그러면 ex) matrix[6][2] = [0,2,3,4,5,0,0,0] 같은 것들이 들어와야할것 같다.
# 그러면 3차원 배열 ,,,? -> 시간복잡도, 공간복잡도 상승으로 이어질 것 같다.
# 그냥 아래와 같이 2차원 배열을 두개 만들도록 하자

connect = [[]for _ in range(N+1)]  # connection information

needs = [[0] * (N+1) for _ in range(N+1)]  # 각 제품을 만들 때 필요한 부품

q = deque()  # 위상 정렬

degree = [0] * (N+1)  # 진입 차수

for _ in range(M):
    a, b, c = map(int, input().split())
    connect[b].append((a, c))  # b를 만드는데 a가 c개 필요하다.
    degree[a] += 1

for i in range(1, N+1):
    # 진입 차수 0 인걸 큐에 넣기
    if degree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    # 현 제품의 다음 단계 번호, 현 제품이 얼마나 필요한지
    for next, next_need in connect[now]:
        # 만약 현 제품이 기본 제품이라면
        if needs[now].count(0) == N+1:
            needs[next][now] += next_need
        # 현 제품이 중간 부품이면
        else:
            for i in range(1, N+1):
                needs[next][i] += needs[now][i] * next_need

        # 차수 -1
        degree[next] -= 1
        if degree[next] == 0:
            # 차수 0 이면 큐에 넣음
            q.append(next)


for x in enumerate(needs[N]):
    if x[1] > 0:
        print(*x)
print(needs)
