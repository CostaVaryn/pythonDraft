'''
Input:
22 18 8
6 11
10 15
3 18
1 19
10 17
1 10
6 16
20 21
1 1
12 21
5 9
1 10
5 10
6 11
5 6
7 11
1 19
13 15
5
22
19
3
8
16
16
21
Output:
8
0
3
5
11
6
6
2
'''

l, n, m = map(int, input().split())
balance = [0] * (l + 1)
ans = [0] * (l + 1)
for i in range(n):
    left, right = map(int, input().split())
    balance[left - 1] += 1
    balance[right] -= 1

now = 0
for i in range(l):
    now = now + balance[i]
    ans[i] = now
for i in range(m):
    query = int(input()) - 1
    print(ans[query])