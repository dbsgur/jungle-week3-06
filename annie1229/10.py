# 10. 연산자 끼워넣기(#14888)
import sys
from copy import deepcopy
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

calc = list(map(int, sys.stdin.readline().split()))
result = [-sys.maxsize, sys.maxsize] # max, min

def dfs(num, checked, index):
    print('-------')
    print('dfs ',num, checked, index)
    if index == N:
        if num > result[0]:
            result[0] = num
        if num < result[1]:
            result[1] = num
        return

    for i in range(4):
        if checked[i] < calc[i]:
            temp = deepcopy(checked)
            temp[i] += 1
            if i == 0: # + 더하기 연산
                print(num + nums[index], '=', num, '+', nums[index])
                dfs(num + nums[index], temp, index + 1)
            elif i == 1: # - 빼기 연산
                print(num - nums[index], '=', num, '-', nums[index])
                dfs(num - nums[index], temp, index + 1)
            elif i == 2: # * 곱하기 연산
                print(num * nums[index], '=', num, '*', nums[index])
                dfs(num * nums[index], temp, index + 1)
            else: # / 나누기 연산
                print(num, '/', nums[index])
                new_num = num
                isMinus = False
                if new_num < 0:
                    isMinus = True
                    new_num *= -1
                new_num //= nums[index]
                print('=', new_num)
                if isMinus:
                    new_num *= -1
                dfs(new_num, temp, index + 1)
            

dfs(nums[0], [0 for _ in range(4)], 1)
print(*result, sep='\n')

    