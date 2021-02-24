arr = list(map(int, input().split()))
dt = int(input())

arr[2] += dt
for i in range(2):
    if arr[2-i] >= 60:
        arr[1-i] += arr[2-i] // 60
        arr[2-i] = arr[2-i] % 60
if arr[0] >= 24:
    arr[0] = arr[0] % 24
print(arr[0], arr[1], arr[2])