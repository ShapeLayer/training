N, m, M, T, R = map(int, input().split())
n = 0
elapsed = 0
now = m
while n < N:
    if now + T <= M:
        now += T
        n += 1
    else:
        if now == m:
            print(-1)
            exit()
        else:
            now = max(now - R, m)
    elapsed += 1
print(elapsed)
