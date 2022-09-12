'''from random import randint'''

def slow(n, tubes):
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                a, b, c = tubes[i], tubes[j], tubes[k]
                if a + b > c and c**2 > a**2 + b**2:
                    ans += 1
    return ans

def fast(n, tubes):
    ans = 0
    for i in range(n):
        l = i + 2
        r = i + 2
        for j in range(i + 1, n):
            while l < n and tubes[i]**2 + tubes[j]**2 >= tubes[l]**2:
                l += 1
            while r < n and tubes[i] + tubes[j] > tubes[r]:
                r += 1
            ans += r - l
    return ans

'''
while True:
    n = 4
    tubes = []
    for i in range(n):
        tubes.append(randint(1, 10))
        tubes.sort()
    print(*tubes)
    ansSlow = slow(n, tubes)
    ansFast = fast(n, tubes)
    print(ansSlow, ansFast)
    if ansSlow != ansFast:
        break
'''

n = int(input())
tubes = list(map(int, input().split()))
print(fast(n, tubes))

"print(slow(n, tubes)"

'''
Input:
4
2 2 3 4
Output:
3
'''