# Sequential Search
n, target = input().split()
n = int(n)
arr = input().split()
for i in range(n):
    if arr[i] == target:
        print(i+1)
        break