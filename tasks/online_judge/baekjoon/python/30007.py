from sys import stdin
input = stdin.readline

for _i in range(int(input())):
    a, b, x = map(int, input().split())
    print(a * (x - 1) + b)
