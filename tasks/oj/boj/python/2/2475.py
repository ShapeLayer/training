puts = map(int, input().split())
sums = 0
for num in puts:
    sums += num**2
print(sums%10)