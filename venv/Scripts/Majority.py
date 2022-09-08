'''
Input:
3
1 2 1
Output:
1

Input:
7
7 5 5 5 5 4 5
Output:
5

Input:
4
3 3 3 1
Output:
3
'''

n = int(input())
nums = list(map(int, input().split()))
cnt = {}
for now in nums:
    cnt[now] = cnt.get(now, 0) + 1
for val in cnt:
    if cnt[val] > n // 2:
        ans = val
print(ans)

# or use this code
#
# n = int(input())
# nums = list(map(int, input().split()))
# nums.sort()
# print(nums[n // 2])

