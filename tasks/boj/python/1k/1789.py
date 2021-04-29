s = int(input())
arr = []
i = 0
while sum(arr) < s:
    i += 1
    arr += [i]
if sum(arr) > s:
    print(len(arr)-1)
else:
    print(len(arr))