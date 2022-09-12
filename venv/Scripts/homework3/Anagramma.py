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

def anagrams(word, words):
    return sorted(word) == sorted(words)
word = input()
words = input()
if anagrams (word, words):
    print('YES')
else:
    print ('NO')

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


