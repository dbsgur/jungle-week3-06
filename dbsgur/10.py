import sys

input = sys.stdin.readline

N = int(input())
A = [int(x) for x in input().split()]
# + - * /
operator = [int(x) for x in input().split()]

results = []


def search(count, result, tors):
    if count == N-1:
        results.append(result)
        return
    count += 1
    if tors[0]:
        tors[0] -= 1
        search(count, result+A[count], tors)
        tors[0] += 1
    if tors[1]:
        tors[1] -= 1
        search(count, result-A[count], tors)
        tors[1] += 1
    if tors[2]:
        tors[2] -= 1
        search(count, result*A[count], tors)
        tors[2] += 1
    if tors[3]:
        tors[3] -= 1
        if result > 0:
            search(count, result//A[count], tors)
        else:
            result *= -1
            search(count, -(result//A[count]), tors)

        tors[3] += 1


search(0, A[0], operator)


print(max(results))
print(min(results))
