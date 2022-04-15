import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

tree = []
count = 0

while True:
    try:
        temp = int(input())
    except:
        break
    tree.append(temp)
    count += 1


def solution(start, end):
    if start > end:
        return
    div = end + 1

    for i in range(start+1, end + 1):
        # 루트보다 큰 지점 --> 오른쪽 서브트리
        if tree[start] < tree[i]:
            div = i
            break

    solution(start+1, div - 1)  # left
    solution(div, end)  # right
    print(tree[start])  # root


solution(0, count - 1)
