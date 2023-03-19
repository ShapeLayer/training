n, m = map(int, input().split())
arr = [i for i in range(n+1)]
for _i in range(m):
    i, j = map(int, input().split())
    arr[i:j+1] = arr[j:i-1:-1]
print(' '.join(map(str, arr[1:])))
