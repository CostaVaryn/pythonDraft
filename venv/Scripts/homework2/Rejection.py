'''
Input:
4
LiTe lite bare Bare
10
Bare BARE Bear bear lite Lite LiTe ...
Output:
Bare bare   lite LiTe LiTe LiTe  LiTe

Input:
1
DeLay
1
delOy
Output:
DeLay
'''

def spellchecker(wordList, queries):
    def unvovel(s):
        s = s.lower()
        for vovel in 'aeiou':
            s = s.replace(vovel, '#')
        return s

    dct = set()
    dctLower = {}
    dctUnvovel = {}
    for word in wordList:
        dct.add(word)
        if word.lower() not in dctLower:
            dctLower[word.lower()] = word
        unvoveled = unvovel(word)
        if unvoveled not in dctUnvovel:
            dctUnvovel[unvoveled] = word
    ans = []
    for word in queries:
        if word in dct:
            ans.append(word)
        elif word.lower() in dctLower:
            ans.append(dctLower[word.lower()])
        elif unvovel(word) in dctUnvovel:
            ans.append(dctUnvovel[unvovel(word)])
        else:
            ans.append("")
    return ans

dctlen = int(input())
dct = list(input().split())
txtlen = int(input())
txt = list(input().split())
print(*spellchecker(dct, txt))
