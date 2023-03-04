n, k = map(int, input().split())
puts = []
for i in range(1, n//2+1):
    if n % i == 0:
        puts += [i]
puts += [n]
if k > len(puts):
    print(0)
else:
    print(puts[k-1])
