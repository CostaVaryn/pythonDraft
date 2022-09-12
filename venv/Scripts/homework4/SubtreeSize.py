'''
Input:
4
1 2
1 3
1 4
Output:
4 1 1 1

Input:
7
1 2
1 3
1 4
5 1
5 6
5 7
Output:
7 1 1 1 3 1 1
'''

import sys

sys.setrecursionlimit(100000)

def dfs(now, neighbors, subtreeSize):
    subtreeSize[now] = 1
    for next in neighbors[now]:
        if subtreeSize[next] == -1:
            subtreeSize[now] += dfs(next, neighbors, subtreeSize)
    return subtreeSize[now]

n = int(input())

neighbors = []
for i in range(n + 1):
    neighbors.append([])

for i in range(n - 1):
    a, b = map(int, input().split())
    neighbors[a].append(b)
    neighbors[b].append(a)

subtreeSize = [-1] * (n + 1)
dfs(1, neighbors, subtreeSize)
print(*subtreeSize[1:])