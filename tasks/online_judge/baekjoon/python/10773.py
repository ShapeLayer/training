from sys import stdin

arr = []
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n == 0:
        if arr:
            arr.pop()
    else:
        arr += [n]
print(sum(arr))
