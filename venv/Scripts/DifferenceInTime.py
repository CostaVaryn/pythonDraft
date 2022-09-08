'''
Input:
2
23:59 00:00
Output:
1

or

Input:
3
00:00 23:59 00:00
Output:
0
'''

n = int(input())

timePoints = input().split()
minutePoints = []
for nowTime in timePoints:
    h, m = map(int, nowTime.split(':'))
    minutePoints.append(h * 60 + m)
minutePoints.sort()
minDist = 24 * 60 + minutePoints[0] - minutePoints[-1]
for i in range(1, len(minutePoints)):
    minDist = min(minDist, minutePoints[i] - minutePoints[i - 1])
print(minDist)