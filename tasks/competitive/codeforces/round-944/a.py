from sys import stdin
input = stdin.readline
for _i in range(int(input())):
    gets = [*map(int, input().split())]
    print(min(gets), max(gets))
