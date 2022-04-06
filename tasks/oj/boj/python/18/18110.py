from sys import stdin
gets = stdin.readline

def rounds(n):
    return int(n) + (1 if n - int(n) >= .5 else 0) 

n = int(input())
if n:
    arr = [int(gets()) for _ in range(n)]
    limits = rounds(n * .15)
    arr.sort()
    if limits != 0:
        arr = arr[limits:-limits]
    if len(arr):
        print(rounds(sum(arr) / len(arr)))
    else:
        print(0)
else:
    print(0)