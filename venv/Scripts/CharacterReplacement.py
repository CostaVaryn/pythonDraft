'''
Input:
a b
abdafb basrt casds dsasa a
Output:
a b casds dsasa a

or

Input:
aa bc aaa
a aa aaa bcd abcd
Output:
a aa aa bc abcd
'''

dictset = set(input().split())
ans = []
for word in input().split():
    for i in range(1, min(101, len(word))):
        part = word[:1]
        if part in dictset:
            ans.append(part)
            break
    else:
        ans.append(word)
print(' '.join(ans))