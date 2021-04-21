from sys import stdin

c = 10000
pl = [True for i in range(c+1)]
pl[0] = False
pl[1] = False
for i in range(2, c+1):
    if pl[i]:
        for j in range(2*i, c+1, i):
            pl[j] = False

n = int(stdin.readline())
for _ in range(n):
    t = int(stdin.readline())
    res = [t//2, t//2]
    while res[0] > 0:
        if pl[res[0]] and pl[res[1]]:
            print(res[0], res[1])
            res[0] = -1
        else:
            res[0] -= 1
            res[1] += 1