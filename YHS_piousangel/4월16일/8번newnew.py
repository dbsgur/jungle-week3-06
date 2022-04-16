import sys
from collections import deque

sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())


def chkWire(wire, visited, idx):

    q = deque()

    visited[wire[idx][0]] = 1       #인덱스 0 왼
    visited[wire[idx][1]] = 2       #오

    q.append(wire[idx])
    wire.remove(wire[idx])
    Trigger = True
    while q:
        
        temp_node = q.popleft()
        flag = False
        left = temp_node[0]   #1
        right = temp_node[1]  #2

        for i in range(len(wire)):
            if Trigger:
                if left == wire[i][0] :   # 왼, 왼
                    if visitd[left] == visited[wire[i][0]]:
                        return False
                    else:
                        visited[wire[i][0]] = 2
                        q.appendleft(wire[i][0])
                        wire.pop(i)
                        Trigger = True
                        flag = True
                
                elif left == wire[i][1] : #왼, 오
                    if visited[left] == visited[wire[i][1]]:
                        return False
                    else:
                        visited[wire[i][1]] = 2
                        q.appendleft(wire[i][1])
                        wire.pop(i)
                        Trigger = True
                        flag = True
                
                elif right == wire[i][0] : # 오, 왼
                    if visited[right] ==  visited[wire[i][0]]:
                        return False
                    else:
                        visited[wire[i][0]] = 1
                        q.appendleft(wire[i][0])
                        wire.pop(i)
                        Trigger = False
                        flag = True
                
                elif right == wire[i][1] : # 오, 오
                    if visited[right] == visited[wire[i][1]]:
                        return False
                    else:
                        visited[wire[i][1]] = 1
                        q.appendleft(wire[i][1])
                        wire.pop(i)
                        Trigger = False
                        flag = True
            else:
                if left == wire[i][0] :
                    if visitd[left] == visited[wire[i][0]]:
                        return False
                    else:
                        visited[wire[i][0]] = 1
                        q.appendleft(wire[i][0])
                        wire.pop(i)
                        Trigger = True
                        flag = True
                
                elif left == wire[i][1] : #왼, 오
                    if visited[left] == visited[wire[i][1]]:
                        return False
                    else:
                        visited[wire[i][1]] = 1
                        q.appendleft(wire[i][1])
                        wire.pop(i)
                        Trigger = True
                        flag = True
                
                elif right == wire[i][0] : # 오, 왼
                    if visited[right] ==  visited[wire[i][0]]:
                        return False
                    else:
                        visited[wire[i][0]] = 2
                        q.appendleft(wire[i][0])
                        wire.pop(i)
                        Trigger = False
                        flag = True
                
                elif right == wire[i][1] : # 오, 오
                    if visited[right] == visited[wire[i][1]]:
                        return False
                    else:
                        visited[wire[i][1]] = 2
                        q.appendleft(wire[i][1])
                        wire.pop(i)
                        Trigger = False
                        flag = True

        if flag :
            i -= 1

    return True      
        

for i in range(n):
    v, e = map(int, input().split())
    wire = []
    visited = [0] * (v+1)
    for i in range(e):
        a, b = map(int, input().split())

        wire.append([a,b])
    
    print(wire)
    
    result = chkWire(wire, visited, 0)
    print(visited)
    if result :
        print("YES")
    else:
        print("NO")
    