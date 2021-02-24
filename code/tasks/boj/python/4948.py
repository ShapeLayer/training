from sys import stdin

c = 246913
pl = [True for i in range(c+1)]
pl[0] = False
pl[1] = False
for i in range(2, c+1):
    if pl[i]:
        for j in range(2*i, c+1, i):
            pl[j] = False

while True:
    n = int(stdin.readline())
    if n == 0:
        break
    cnt = 0
    for i in range(n+1, 2*n+1):
        if pl[i]:
            cnt += 1
    print(cnt)