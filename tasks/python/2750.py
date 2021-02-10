## Not Confirmed

from sys import stdin
n = int(stdin.readline())

li = []
for i in range(n):
    t = int(stdin.readline())
    if not li:
        li += [t]
    else:
        le = [0, len(li)]
        loop = True
        while loop:
            c = le[0] + le[1]//2
            if t == li[c]:
                loop = False
            elif t < li[c]:
                if t < li[c] and t > li[c-1]:
                    li.insert(li.index(li[c])-1, t)
                    loop = False
                else:
                    le[1] = li[c]
            else:
                if t < li[c+1] and t > li[c]:
                    li.insert(li.index(li[c])-1, t)
                    loop = False
                else:
                    le[0] = li[c]