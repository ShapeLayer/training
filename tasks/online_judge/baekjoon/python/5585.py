n = 1000 - int(input())
cnt = 0
for dt in (500, 100, 50, 10, 5, 1):
    cnt += n // dt
    n %= dt
print(cnt)
