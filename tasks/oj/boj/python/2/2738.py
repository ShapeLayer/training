n, m = map(int, input().split())
arr = [[] for _i in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))
for i in range(n):
    gets = list(map(int, input().split()))
    for j in range(m):
        arr[i][j] += gets[j]
for i in range(n):
    print(' '.join(map(str, arr[i])))
