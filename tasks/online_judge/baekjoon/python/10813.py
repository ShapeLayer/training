n, m = map(int, input().split())
arr = [i for i in range(n+1)]
for _i in range(m):
    i, j = map(int, input().split())
    arr[i], arr[j] = arr[j], arr[i]
print(' '.join(map(str, arr[1:])))
