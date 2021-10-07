arr = []
for i in range(int(input())):
    arr += [int(input())]
arr = sorted(arr, reverse=True)
print(' '.join(list(map(str, arr))))