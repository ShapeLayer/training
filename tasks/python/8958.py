from sys import stdin
r = int(stdin.readline())

for i in range(r):
    his = stdin.readline().rstrip()
    p = 0
    s = 0
    for j in range(len(his)):
        if his[j] == 'O':
            s += 1
            p += s
        else:
            s = 0
    print(p)