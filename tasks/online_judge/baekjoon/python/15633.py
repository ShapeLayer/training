n = int(input())
arr = []
for i in range(1, n+1):
    if n % i == 0:
        arr += [i]
print(sum(arr) * 5 - 24)
