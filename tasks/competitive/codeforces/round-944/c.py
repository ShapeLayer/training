from sys import stdin
input = stdin.readline

for _i in range(int(input())):
    a, b, c, d = map(int, input().split())
    arr = [each[1] for each in sorted([(a, 0), (b, 0), (c, 1), (d, 1)])]
    if arr[0] == arr[1] or arr[1] == arr[2] or arr[2] == arr[3] or arr[3] == arr[0]:
        print('NO')
    else:
        print('YES')
