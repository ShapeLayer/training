from sys import stdin
arr = []
for _ in range(9):
    arr += [int(stdin.readline())]
s = sum(arr)
r = []
for i in range(0, 8):
    for j in range(i+1, 9):
        if (s - arr[i] - arr[j]) == 100:
            r = [i, j]
arr.pop(r[0])
arr.pop(r[1]-1)
arr.sort()
for tall in arr:
    print(tall)