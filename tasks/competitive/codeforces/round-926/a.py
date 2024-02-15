from sys import stdin
input = stdin.readline

for _i in range(int(input())):
    n = int(input())
    arr = [*map(int, input().split())]
    print(max(arr) - min(arr))
