from sys import stdin
input = stdin.readline

for _i in range(int(input())):
    a, b = map(int, input().split())
    print((a ** 2) // (b ** 2))
