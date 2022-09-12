'''
Input:
5
2 -1 2 -2 3
4
1 1
1 3
2 4
1 5
Output:
1
2
1
3
'''

n = int(input())
nums = list(map(int, input().split()))
prPos = [0]
for i in range(n):
    if nums[i] > 0:
        prPos.append(prPos[-1] + 1)
    else:
        prPos.append(prPos[-1])

q = int(input())
for i in range(q):
    f, t = map(int, input().split())
    print(prPos[t] - prPos[f - 1])