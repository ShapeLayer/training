from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
char = [set() for _i in range(n)]
combs = []
dic = {}
for _i in range(m):
    gets = input().strip()
    for i in range(n):
        char[i].add(gets[i])
    if gets in dic:
        print('NO')
        exit()
    dic[gets] = True

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if len(char[i] & char[j]) > 0:
            print('NO')
            exit()

char = [sorted(list(each)) for each in char]

def match(i = 0, build = []):
    if i == n:
        return ''.join(build) in dic
    for each in char[i]:
        if not match(i + 1, build + [each]):
            return False
    return True

if match():
    print('YES')
    for i in range(n):
        print(''.join(char[i]))
else:
    print('NO')
