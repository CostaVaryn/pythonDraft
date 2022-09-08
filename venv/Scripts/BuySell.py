'''
Input:
6
10 3 5 3 11 9
Output:
2 5

or

Input:
4
5 5 5 5
Output:
0 0
'''

n = int(input())
cost = list(map(int, input().split()))

bestBuyDay = 0
bestSellDay = 0
minCostDay = 0
for i in range(1, n):
    if cost[bestSellDay] * cost[minCostDay] < cost[bestBuyDay] * cost[i]:
        bestBuyDay = minCostDay
        bestSellDay = i
    if cost[i] < cost[minCostDay]:
        minCostDay = i
if bestSellDay == 0 and bestBuyDay == 0:
    print(0, 0)
else:
    print(bestBuyDay + 1, bestSellDay + 1)


minIndex = 0
maxGas = 1000 / cost[0]
maxRevenue = 0
ans = (0, 0)
for i in range(1, n):
    if maxGas * cost[i] - 1000 > maxRevenue:
        maxRevenue = maxGas * cost[i] - 1000
        ans = (minIndex + 2, i + 1)
    if 1000 / cost[i] > maxGas:
        mixIndex = i
        maxGas = 1000 / cost[i]
print(*ans)
