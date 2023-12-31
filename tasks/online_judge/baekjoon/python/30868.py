from sys import stdin
input = stdin.readline

for _i in range(int(input())):
    n = int(input())
    print(' '.join(['++++' for _i in range(n // 5)] + [''.join(['|' for _i in range(n % 5)])]))
