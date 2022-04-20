# 1. 섬마다 가장자리를 구한다.
# 2. 가장 자리에서 뻗는다.
# 3. 다른 섬이랑 닿았나 ? 확인한다.
#     👆 이걸하려면 1번 과정에서섬의 번호와 그 섬의 좌표들을 저장해야할듯?
# 4. 차이가 2이상인지 확인한다.
# 👆위처럼 하고 싶은데
# 1번부터 모르겠다. 그래서 나와 가장 풀이가 비슷한 사람의 코드를 가져왔다.

###############################################################

# URL : https://westmino.tistory.com/149
# 1. BFS로 각 섬에  번호 매기면서 섬의 가장자리를 구한다.
# 이 때, 해당 점에서 이동하려는 점이 격자판 안에 있고, 물인 경우 가장자리로 판별해서 저장
# 2. 구한 가장자리에서 다리를 만들면서 유효한 다리 정보를 생성한다.
# 이 때는 구한 가장잘이ㅢ 정보를 가지고 다리를 생성한다.(!?)
# 3. 저장한 방향정보를 가지고 범위를 벗어나거나 다른 섬을 만날때까지 진행한다.
# 다른 섬을 만났다면 다리 정보를 생성한다.
# (출발 다리 번호, 도착 다리 번호, 길이)
# 다리 정보를 길이순으로 오름차순으로 정렬해서 MST에 사용하자
# MST - 크루스칼
from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
edges = []


def solv():
    global parent
    max_num = set_area_num()

    parent = [i for i in range(max_num)]
    candidate_bridge = set_candidate_bridge()

    print(kruskal(candidate_bridge, max_num))

## KRUSKAL ALGORITHMS START ##


def kruskal(candidate_bridge, max_num):
    bridge_count = 0
    length = 0

    for a, b, c in candidate_bridge:
        if not is_same_parent(a, b):
            union(a, b)
            bridge_count += 1
            length += c
            if bridge_count == max_num-3:
                return length
    return -1


def find(target):
    # global parent
    if parent[target] == target:
        return target
    parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    # global parent
    a = find(a)
    b = find(b)

    if a != b:
        if a > b:
            parent[a] = b
        else:
            parent[b] = a


def is_same_parent(a, b):
    return find(a) == find(b)

## KRUSKAL ALGORITHMS END ##

# 다리 생성


def set_candidate_bridge():
    candidate_bridge = set()
    for x, y, d in edges:
        start = board[x][y]
        length = 0
        while True:
            x += dx[d]
            y += dy[d]
            if boundaray_validator(x, y):
                end = board[x][y]
                if end != 0:
                    # 길이 2이상인지 확인
                    if start != end and length >= 2:
                        candidate_bridge.add((start, end, length))
                    break
                length += 1
            else:
                break

    candidate_bridge = sorted(candidate_bridge, key=lambda x: x[2])
    return candidate_bridge

# bfs로 섬 갯수 세기


def set_area_num():
    num = 2
    for x in range(n):
        for y in range(m):
            if board[x][y] == 1:
                bfs(x, y, num)
                num += 1
    return num


def bfs(sx, sy, num):
    # global board, edges
    q = deque([(sx, sy)])
    board[sx][sy] = num

    while q:
        x, y = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if boundaray_validator(nx, ny):
                if board[nx][ny] == 1:
                    board[nx][ny] = num
                    q.appendleft((nx, ny))
                elif board[nx][ny] == 0:
                    edges.append((x, y, d))

# 격자 벗어난 건지


def boundaray_validator(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return True


solv()
