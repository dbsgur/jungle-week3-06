import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

N, M = map(int, input().split())

marble = [[0]*(N+1) for _ in range(N+1)]

# 모르겠다옹 ~
