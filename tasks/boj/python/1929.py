from sys import stdin
m, n = list(map(int, stdin.readline().split()))


pl = [True for i in range(n+1)]
pl[0] = False
pl[1] = False
for i in range(2, n+1):
    for j in range(2, n//i+1):
        pl[i*j] = False

for i in range(m, n+1):
    if pl[i]:
        print(i)