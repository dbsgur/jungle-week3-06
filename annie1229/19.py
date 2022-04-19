# 19. 동전 2(#2294)
import sys
from collections import deque
sys.stdin = open('input.txt')

n, k = map(int, sys.stdin.readline().split())
coins = set() # 같은 동전이 여러번 주어질 수 있기 때문에 set으로 받는다
check = [0 for _ in range(k + 1)] # 0~k까지 확인할 check 배열을 만든다.

for _ in range(n):
    coins.add(int(sys.stdin.readline()))

def bfs():
    q = deque()
    
    for coin in coins:
        if coin > k: # 합계보다 큰 동전은 패스
            continue
        q.append([coin, 1]) # 큐에 [가치, 사용 갯수] 넣기
        check[coin] = 1 # 해당 가치 확인 여부 체크
    
    while q:
        pop = q.popleft()
        if pop[0] == k: # 만약 원하는 합계랑 똑같은 값이 나오면 사용 개수 출력하고 함수 종료
            print(pop[1])
            return

        for coin in coins:
            if coin + pop[0] > k:
                continue
            if check[coin + pop[0]] == 0: # 아직 만들어보지 않은 가치면
                check[coin + pop[0]] = 1 # 확인 했다고 체크
                q.append([coin + pop[0], pop[1] + 1]) # 큐에 [가치 합계, 사용 갯수] 넣기

    print(-1) # 끝까지 k와 똑같은 값이 안나왔으면 -1 출력 

bfs()