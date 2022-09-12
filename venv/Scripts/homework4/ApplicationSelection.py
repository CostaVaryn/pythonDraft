'''
Input:
3
5 10
Output:
1

Input:
3
1 5
2 3
3 4
Output:
2
'''

requests = []
n = int(input())
for i in range(n):
    s = list(map(int, input().split()))
    requests.append(s)
cnt = 1
requests.sort(key=lambda x: x[1])
end = requests[0][1]
for i in range(1, n):
    if requests[i][0] >= end:
        cnt += 1
        end = requests[i][1]
print(cnt)