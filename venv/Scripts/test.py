def slow(n, tubes):
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                a, b, c = tubes[i], tubes[j], tubes[k]
                if a + b > c and c**2 > a**2 + b**2:
                    ans += 1
    return ans

n = int(input())
tubes = list(map(int, input().split()))
print(slow(n, tubes))

'''
Input:
4
2 2 3 4
Output:
3
'''