'''
Input:
dusty
study
Output:
YES

Input:
rat
bat
Output:
NO
'''

import sys
word = sys.stdin.readline()
words = sys.stdin.readline()
def anagrams(word, words): return "YES" if sorted(word)==sorted(words) else "NO"
print(anagrams(word, words))


'''
valide code

def check(s1, s2):
    if(sorted(s1) == sorted(s2)):
        print("YES")
    else:
        print("NO")
s1 = list(input().split())
s2 = list(input().split())
check(s1, s2)
'''


'''
def anagram(str1, str2):
    str1 = int(input())
    str2 = int(input())
    if str1 != str2:
        return print("NO")

    str1 = sorted(str1)
    str2 = sorted(str2)
    for i in range(0, str1):
        if str1[i] != str2[i]:
            return print("YES")
    return 1
'''


