import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

R, C = map(int, input().split())

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

forest = [[x for x in input().strip()]for _ in range(R)]

print(forest)
