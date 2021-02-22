k, n, m = list(map(int, input().split()))
need = k*n-m
if need < 0:
    print(0)
else:
    print(need)