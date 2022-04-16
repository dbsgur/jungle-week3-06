import sys
from collections import deque

sys.stdin = open("input.txt")

input = sys.stdin.readline

N = int(input())

M = int(input())

realations = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    # X : 완제품 / Y : 필요 제품 / K : 필요한 갯수
    X, Y, K = map(int, input().split())
    realations[X][Y] = K

indegree = [0] * (N+1)

dq = deque()
