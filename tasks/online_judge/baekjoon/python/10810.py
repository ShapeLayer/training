n, m = map(int, input().split())
arr = [0 for _i in range(n+1)]
for _i in range(m):
    i, j, k = map(int, input().split())
    for l in range(i, j+1):
        arr[l] = k
print(' '.join(map(str, arr[1:])))
