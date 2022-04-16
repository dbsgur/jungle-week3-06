# 2. 이진 검색 트리(#5639)
import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input.txt')

bst = []

def postorder(left, right):
    if left > right:
        return
    
    mid = right + 1
    root = bst[left]

    for i in range(left + 1, right + 1):
        if bst[i] > root: # root 값을 처음 넘어가는 숫자를 기준으로 왼쪽 서브트리, 오른쪽 서브트리 자르기
            mid = i
            break
    
    postorder(left + 1, mid - 1)
    postorder(mid, right)
    print(bst[left]) # 후위 순회 출력

while True:
    num = sys.stdin.readline()
    if num:
        bst.append(int(num))
    else:
        postorder(0, len(bst) - 1)
        break

