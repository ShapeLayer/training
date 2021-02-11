from sys import stdin
m = int(stdin.readline())
n = int(stdin.readline())


pl = [True for i in range(10001)]
pl[0] = False
pl[1] = False
for i in range(2, 10001):
    for j in range(2, 10000//i+1):
        pl[i*j] = False

li = []
for i in range(m, n+1):
    if pl[i]:
        li += [i]

if li:
    print(sum(li))
    print(min(li))
else:
    print(-1)