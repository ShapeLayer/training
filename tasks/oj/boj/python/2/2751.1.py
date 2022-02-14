from sys import stdin
puts = stdin.readline

arr = []
for i in range(int(puts())):
    arr += [int(puts())]
for i in sorted(arr):
    print(i)