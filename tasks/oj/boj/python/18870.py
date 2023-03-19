n = int(input())
arr = list(map(int, input().split()))
conn = {}
arr_sorted = sorted(arr)
prev = None
offset = 0
for i in range(n):
    if prev != None:
        if prev == arr_sorted[i]:
            offset += 1
    prev = arr_sorted[i]
    conn[arr_sorted[i]] = i - offset
print(' '.join(map(str, map(lambda x: conn[x], arr))))
