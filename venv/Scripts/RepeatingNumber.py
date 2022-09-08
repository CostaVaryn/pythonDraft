'''
Input:
4 2
1 2 3 1
Output:
NO

or

Input:
4 1
1 0 1 1
Output:
YES
'''

def sol(nums, k):
    lastk = set()
    for i in range(len(nums)):
        if nums[i] in lastk:
            return True
        lastk.add(nums[i])
        if i >= k:
            lastk.remove(nums[i - k])
    return False

n, k = map(int, input().split())
nums = list(map(int, input().split()))
