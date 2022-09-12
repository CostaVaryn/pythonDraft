'''
Input:
2
16 16
Output:
2

Input:
3
17 16 18
Output:
2
'''

def numFriendRequests(n, ages):
    ages.sort()
    left = 0
    right = 0
    ans = 0
    for i in range(n):
        while left < n and ages[left] <= 0.5 * ages[i] + 7:
            left += 1
        while right < n and ages[right] <= ages[i]:
            right += 1
        if right > left + 1:
            ans += right - left - 1
    return ans

n = int(input())
ages = list(map(int, input().split()))
print(numFriendRequests(n, ages))