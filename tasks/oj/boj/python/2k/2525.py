arr = list(map(int, input().split()))
dt = int(input())

arr[1] += dt
if arr[1] >= 60:
    arr[0] += arr[1] // 60
    arr[1] = arr[1] % 60
if arr[0] >= 24:
    arr[0] = arr[0] % 24
print(arr[0], arr[1])