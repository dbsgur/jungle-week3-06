import sys
from collections import deque

sys.stdin = open("input.txt")

input = sys.stdin.readline

N = int(input())

roads = [int(x) for x in input().split()]

prices = [int(x) for x in input().split()]

price = 1e9
result = 0
for i in range(N-1):
    price = min(price, prices[i])
    result += price * roads[i]

print(result)
