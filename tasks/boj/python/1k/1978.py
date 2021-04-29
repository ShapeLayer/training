from sys import stdin
n = int(stdin.readline())
nl = list(map(int, stdin.readline().split()))

pl = [True for i in range(1001)]
pl[0] = False
pl[1] = False
for i in range(2, 1001):
    for j in range(2, 1000//i+1):
        pl[i*j] = False

cnt = 0
for i in range(n):
    if pl[nl[i]]:
        cnt += 1

print(cnt)