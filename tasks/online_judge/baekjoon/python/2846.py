n = int(input())
arr = [*map(int, input().split())]

prev = arr[0]
starts = arr[0]
res = 0

for each in arr[1:]:
    if prev < each:
        res = max(res, each - starts)
    else:
        res = max(res, prev - starts)
        starts = each
    prev = each
print(res)
