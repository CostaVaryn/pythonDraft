def slow(n):
    nowinrow = 1
    rows = 0
    while n >= nowinrow:
        n -= nowinrow
        rows += 1
        nowinrow += 1
    return rows

n = int(input())
print(slow(n))

'''
Input:
5
Output:
2

or

Input:
8
Output:
3
'''