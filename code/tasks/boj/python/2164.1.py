n = int(input())
arr = [i for i in range(1, n+1)]
while len(arr) != 1:
    if len(arr) % 2 == 0:
        arr = arr[1::2]
    else:
        arr = [arr[len(arr)-1]] + arr[1::2]
print(arr[0])