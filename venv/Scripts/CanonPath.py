def simplyfyPath(path: str) -> str:
    flag = True
    path += '/'
    while flag:
        if '/./' in path:
            path = path.replace('/./', '/')
            flag =True
        elif '//' in path:
            path = path.replace('//', '/')
        elif '/../' in path:
            path = path.find('/../')
            if pos == 0:
                path = path[3:]
            else:
                prevslashpos = path.rfind('/', 0, pos - 1)
                path = path[:prevslashpos] + path[pos + 3:]
        else:
            flag = False
    if path.endswith('/') and path != '/':
        path = path[:-1]
    if path.endswith('/.'):
        path = path[:-2]
    if path == '':
        path = '/'
    return path

s = input()
print(simplyfyPath(s))

'''
Input: /home/
Output: /home

Input: /../
Output: /

Input: /home//foo/
Output: /home/foo
'''