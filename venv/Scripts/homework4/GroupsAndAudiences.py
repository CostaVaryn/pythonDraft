'''
Input:
3
3 1 2
2
1 1
Output:
1

Input:
2
1 2
3
3 2 1
Output:
2
'''

def sol(groups, auds):
    groups.sort()
    auds.sort()
    pos = 0
    ans = 0
    for now in groups:
        while pos < len(auds) and auds[pos] < now:
            pos += 1
        if pos != len(auds):
            ans += 1
            pos += 1
    return ans

n = int(input())
groups = list(map(int, input().split()))
m = int(input())
auds = list(map(int, input().split()))
print(sol(groups, auds))