'''
Input:
2
3 1
2
1 3
2
1 2
Output:
1 3

or

Input:
3
1 2 2
3
3 4 3
1
5
Output:

'''

l1 = input()
s1 = set(map(int, input().split()))
l2 = input()
s2 = set(map(int, input().split()))
l3 = input()
s3 = set(map(int, input().split()))
ans = s1 & s2
merged12 = s1.union(s2)
ans = ans.union(merged12 & s3)
print(*sorted(ans))