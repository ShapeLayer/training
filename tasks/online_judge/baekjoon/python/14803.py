from sys import stdin
input = stdin.readline

t = int(input())
for tc in range(t):
    d, n = map(int, input().split())
    horses = sorted([[*map(int, input().split())] for _j in range(n)])
    hours = -1
    for i in range(n):
        hours = max(hours, (d - horses[i][0]) / (horses[i][1]))
    print('Case #%d: %.6lf' % (tc + 1, d / hours))
