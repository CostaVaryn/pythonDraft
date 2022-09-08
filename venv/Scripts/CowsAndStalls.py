'''
Input:
6 3
2 5 7 11 15 20
Output:
9
'''

'''
n, k = map(int, input().split())
coords = list(map(int, input().split()))
def check(x):
    cows = 1
    lastcow = coords[0]
    for i in coords:
        if i - lastcow >= x:
            cows += 1
            lastcow = i
    return cows >= k
def solve():
    left = 0
    right = coords[-1] - coords[0] + 1
    m = (left + right) // 2
    if check(m):
        left = m
    else:
        right = m
    return left
print(solve())

'''
n, k = map(int, input().split())
*a, = map(int, input().split())
a.sort()
left = 0
right = a[-1] - a[0] + 1
while left < right:
    mid = (left + right)//2
    cows = 1
    last = a[0]
    for cur in a[1:]:
        if cur - last > mid:
            cows += 1
            last = cur
    if cows >= k:
        left = mid+1
    else:
        right = mid
print(left)
