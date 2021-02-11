from sys import stdin
from sys import stdout

n = int(stdin.readline())

if n < 100:
    print(n)
else:
    cnt = 99
    for i in range(100, n+1):
        t = i
        arr = []
        a = t // 100
        arr += [a]
        t -= a * 100
        a = t // 10
        arr += [a]
        t -= a * 10
        arr += [t]
        if arr[0]-arr[1] == arr[1]-arr[2]:
            cnt += 1
    print(cnt)