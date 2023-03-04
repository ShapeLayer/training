from sys import stdin
input = stdin.readline
n, m, q = map(int, input().split())
arr = []
for _i in range(n):
    arr.append(list(map(int, input().split())))
for _i in range(q):
    gets = list(map(int, input().split()))
    if gets[0] == 0:
        qu, i, j, k = gets
        arr[i][j] = k
    else:
        qu, i, j = gets
        arr[i], arr[j] = arr[j], arr[i]
buf = []
for i in range(n):
    buf.append(' '.join(map(str, arr[i])))
print('\n'.join(buf))
