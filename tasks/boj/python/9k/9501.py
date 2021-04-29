from sys import stdin
for _ in range(int(stdin.readline())):
    n, d = list(map(int, stdin.readline().split()))
    cnt = 0
    for i in range(n):
        v, f, c = list(map(int, stdin.readline().split()))
        if (d/v)*c <= f:
            cnt += 1
    print(cnt)