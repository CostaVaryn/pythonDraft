'''
Input:
1.avi
12
emoh
 vonavi
  a.doc
  b.doc
 vortep
  .bashrc
 vorodis
  onrop
   1.avi
   2.avi
rav
 bil

Output:
/emoh/vorodis/onrop/1.avi
'''

query = input()
n = int(input())
fname = {}
nowpath = []
for i in range(n):
    line = input()
    nowFile = line.strip()
    spaces = 0
    while spaces < len(line) and line[spaces] == ' ':
        spaces += 1
    nowpath = nowpath[:spaces]
    nowpath.append(nowFile)

    if nowFile not in fname:
        fname[nowFile] = '/' + '/'.join(nowpath)
print(fname[query])

    #if nowFile == query:
    #    print('/' + '/'.join(nowpath))
    #    break
