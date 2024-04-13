from sys import stdin
input = stdin.readline

for _i in range(int(input())):
    n, k = map(int, input().split())
    if k <= 4 * (n - 1):
        print((k + 1) // 2)
    elif k == 4 * n - 3:
        print(4 * n - 2)
    elif k == 4 * n - 2:
        print(k // 2 + 1)
