n = int(input())
arr = [-1 for i in range(max(n + 1, 4))]
arr[1], arr[2], arr[3] = 1, 2, 2

for i in range(4, n + 1):
    now = arr[i-1] + 1
    if i % 2 == 0: now = min(now, arr[i // 2] + 1)
    if i % 3 == 0: now = min(now, arr[i // 3] + 1)
    arr[i] = now

i = n
buf = []
while i != 1:
    buf.append(i)
    if i % 3 == 0 and arr[i // 3] + 1 == arr[i]:
        i //= 3
    elif i % 2 == 0 and arr[i // 2] + 1 == arr[i]:
        i //= 2
    else:
        i -= 1
buf.append(1)

print(len(buf) - 1)
print(' '.join(map(str, buf)))
