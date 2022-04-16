import sys
from collections import deque

sys.stdin = open("input.txt")

input = sys.stdin.readline

N = int(input())

M = int(input())

realations = []

for _ in range(M):
    X, Y, K = map(int, input().split())
